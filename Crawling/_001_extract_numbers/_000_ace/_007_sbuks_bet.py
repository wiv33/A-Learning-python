import datetime
import json
import os
import re
import sys
from dataclasses import dataclass
import requests

from SbucksKafkaManager import SbucksKafkaManager, PB_5_TOPIC, PB_5_TOPIC_TEST, SUBMIT_BET_5_TOPIC, ACCESS_LOG_TOPIC
import random
import time

from selenium.webdriver.common.by import By

from BrowserModule import Browser, user_path
import pandas as pd


@dataclass
class Bet:
    def __init__(self, _amount, _choice):
        self.amount = _amount
        self._choice = _choice
        self.victory = False

    def is_victory(self, result):
        print(f"choice: {self._choice}, result: {result}")
        self.victory = self._choice == result
        return self.victory

    def next_bet(self, _init_amount, _result, _next_choice: str, _ratio):
        if not _result or self.is_victory(_result.strip()):
            return Bet(_init_amount, _next_choice)

        return Bet(self.amount * _ratio, _next_choice)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return '({}, {}, {})'.format(self.amount, self._choice, self.victory)


class BetsManager:
    def __init__(self, _service: Browser, _k_manager: SbucksKafkaManager, _bet_group_id: str):
        self.prev_algo = ''
        self.algo = ''
        self.total_amount = 0
        self.number = None
        self.powerball = None
        self._tab_cnt = 17
        self._minimum_amount = 100
        self._ratio = 2.3

        self._bet_group_id = _bet_group_id
        self._service = service
        self._k_manager = _k_manager

        self._tabs = []

        self._account_df = pd.read_csv(user_path('account.csv'))
        self._df = pd.read_csv(user_path('gb_url.csv'))
        self.url = self._df.iloc[1].url
        self.bet_url = self._df.iloc[1].bet_url

    def login_sbuks(self):
        print(self._account_df.iloc[0])
        self._service.wait_selector("#username").send_keys(self._account_df.iloc[0].username)
        self._service.wait_selector("#password").send_keys(self._account_df.iloc[0].password)
        self._service.wait_selector(".btn_login").click()

    def choice(self):
        selector_all = self._service.wait_selector_all(
            ".powerball_row:nth-child(n + 4):nth-child(-n + 7) label "
            "span:nth-child(1)")
        choice = random.choice(selector_all)
        self._service.d.execute_script("arguments[0].click();", choice)
        _res = re.sub('[^A-Za-z가-힣]', '', choice.text)
        print("random choice result:", _res)
        return _res

    def setup_tabs(self):
        print("setup_tabs")

        self.open_tabs()

        for k in self._service.d.window_handles:
            print("append tab")
            self._tabs.append((k, Bet(self._minimum_amount, "")))

        print(f"tabs len: {len(self._tabs)}, {self._tabs}")

    def open_tabs(self):
        for _ in range(1, self._tab_cnt):
            self._service.d.execute_script(f"window.open('{self.bet_url}')")
            print("success new tab ", _)

    def _bet_update(self, msg):
        print(f"_bet_update : {msg}")
        self.prev_algo = self.algo
        self.algo = msg['algo']
        self.powerball = msg['power']
        self.number = msg['number']

    def submit(self, tab, _bet) -> Bet:
        self._service.d.switch_to.window(tab)
        choice_text = self.choice()

        _bet_next = _bet.next_bet(self._minimum_amount, self.prev_algo, choice_text, self._ratio)
        self._service.wait_selector('idCartBetMoney', by=By.ID).clear()
        self._service.wait_selector('idCartBetMoney', by=By.ID).send_keys(_bet_next.amount)

        submit_btn = self._service.wait_selector('.btn_betting_confirm')
        self._service.d.execute_script("arguments[0].click();", submit_btn)
        time.sleep(1)
        self._service.d.switch_to.alert.accept()
        time.sleep(1)
        try:
            if self._service.d.switch_to.alert:
                print(self._service.d.switch_to.alert.text)
                time.sleep(2)
                self._service.d.switch_to.alert.accept()
                print("exists alert")
                try:
                    if str(self._service.d.switch_to.alert.text).startswith("조금 전에 주문하셨습니다."):
                        self._service.d.switch_to.alert.accept()
                        time.sleep(2)
                except Exception as __e:
                    if __e.__str__() != 'no such alert':
                        print(__e)

                _bet_next = Bet(self._minimum_amount, choice_text)
            else:
                print("not exists alert")

        except Exception as _e:
            print("submit exception: ", _e)
            print("publish bet")
            self._k_manager.publish_message(SUBMIT_BET_5_TOPIC, _bet_next.to_json(), f"{self._bet_group_id}:{tab}")

        return _bet_next

    def _step(self, tab, _bet):
        print("tabs k is ", tab)

        _bet_next = self.submit(tab, _bet)

        self._tabs.remove((tab, _bet))
        self._tabs.append((tab, _bet_next))

        print("tabs len: ", self._tabs.index((tab, _bet)), _bet.to_json(), _bet_next.to_json())

    def _next(self):
        print("next bet")
        print(self._tabs)
        exec_cnt = 0
        for tab, _bet in self._tabs:
            self._step(tab, _bet)
            exec_cnt += 1

        print(exec_cnt)

    def run(self, msg):
        self._bet_update(msg)
        self._next()


if __name__ == '__main__':
    # {'date': '2023-01-08', 'algo': '287975504/FDB1A (215)',
    # 'power': {'result': '4', 'section': 'B', 'odd_even': '짝', 'under_over': '언더'},
    # 'number': {'result': '26 14 12 15 22', 'sum': '89', 'section': 'F', 'size': '대', 'odd_even': '홀', 'under_over':
    # '오버'}}
    MINIMUM_AMOUNT = 100

    service = Browser('chrome', view_mode=True)

    bet_group_id = 'sun18'
    if len(sys.argv) > 1:
        bet_group_id = sys.argv[1]
        print("update group id : ", bet_group_id)

    k_manager = SbucksKafkaManager()
    access_id = f"{bet_group_id}:{os.getpid()}:{requests.get('https://api.ip.pe.kr/').text}"
    k_manager.publish_message(ACCESS_LOG_TOPIC, access_id, 'login')
    bet = BetsManager(service, k_manager, bet_group_id)
    service.d.get(bet.url)

    try:
        print("start bet")
        bet.login_sbuks()
        time.sleep(1)
        service.d.execute_script(f"location.href = '{bet.bet_url}';")
        bet.setup_tabs()

        k_manager.consume_loop(PB_5_TOPIC_TEST, bet_group_id, bet.run)
        print(bet.total_amount)

        time.sleep(15)

    except Exception as e:
        print(f'{e}')
    finally:
        k_manager.publish_message(ACCESS_LOG_TOPIC, access_id, 'logout')
        service.d.quit()
