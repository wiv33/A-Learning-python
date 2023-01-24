import json
import re
import time
import schedule

import pandas as pd
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_selector(d, selector, wait_time=5, by=By.CSS_SELECTOR):
    return WebDriverWait(d, wait_time).until((
        ec.presence_of_element_located(
            (by, selector)
        )
    ))


def wait_selector_all(d, selector, wait_time=5, by=By.CSS_SELECTOR):
    return WebDriverWait(d, wait_time).until((
        ec.presence_of_all_elements_located(
            (by, selector)
        )
    ))


_subnet = "ps_v1_"
type_result = {
    "POWER_OE": "[EOS]",
    "POWER_UO": "[EOS]",
    "BASIC_OE": "[일반불]",
    "BASIC_UO": "[일반불]"
}
type_idx = {
    "POWER_OE": 0,
    "BASIC_OE": 0,
    "POWER_UO": 0,
    "BASIC_UO": 0
}

MIN_AMOUNT = 100
MAX_AMOUNT = 1_000_000

df = pd.read_csv("info.csv")
server_df = pd.read_csv("server.csv")
_id, cnt = df.iloc[0]
_host, _conn_url = server_df.iloc[0]


def steps(_type):
    next_steps(_type)
    schedule.every(5).minutes.do(next_steps, _type)


if __name__ == '__main__':
    def next_steps(_type):
        for idx in range(cnt):
            response = get_next_response(_type, idx)

            result = response
            print("batting info", result)
            _curr_amount = result['amount']
            _curr_choice = result['choice']

            selector_json = {
                "POWER_OE": {
                    "ODD": "#span_4",
                    "EVEN": "#span_5"
                },
                "BASIC_OE": {
                    "ODD": "#span_0",
                    "EVEN": "#span_1"
                },
                "POWER_UO": {
                    "UNDER": "#span_6",
                    "OVER": "#span_7",
                },
                "BASIC_UO": {
                    "UNDER": "#span_2",
                    "OVER": "#span_3",
                }
            }
            print("result : ", result)
            _next_amount, _next_type, _next_choice = result['amount'], result['fiveType'], result['choice']
            b.execute_script("(function(){ window.print_y = 'Y'})();")
            b.execute_script(f'bat_money_change2({_next_amount})')
            bat_btn = b.find_element(By.CSS_SELECTOR, selector_json[_next_type][_next_choice])
            b.execute_script("arguments[0].click();", bat_btn)
            b.execute_script(f'javascript:buy_ok()')
            print("=" * 33)
            print(
                f"\t\t배팅 금액: {_next_amount}\n"
                f"\t\t배팅 타입: {_type}\n"
                f"\t\t배팅 선택: {_next_choice}")
            print("=" * 33)
            try:
                if b.switch_to.alert:
                    print(b.switch_to.alert.text)
                    time.sleep(2)
                    b.switch_to.alert.accept()
                    print("exists alert")
                    try:
                        if b.switch_to.alert:
                            time.sleep(2)
                            b.switch_to.alert.accept()
                    except Exception as __e:
                        if __e.__str__() != 'no such alert':
                            print(__e)
                else:
                    print("not exists alert")
            except Exception as _e:
                if not _e.__str__().lower().__contains__('no such alert'):
                    print(_e)
            b.refresh()
            time.sleep(7)


    def get_next_response(_type, idx):
        # _subnet_result = _subnet + "_" + str(idx)
        # base_url = f"{_host}{_conn_url.replace('{conn}', _id).replace('{sub}', _subnet_result).replace('{type}', _type)}"
        # response = requests.get(base_url, verify=False)
        # print(base_url)
        assert idx < 12
        type_map = {
            "POWER_OE": ["ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN"],
            "POWER_UO": ["UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER",
                         "OVER"],
            "BASIC_OE": ["ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN"],
            "BASIC_UO": ["UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER",
                         "OVER"],
        }
        convert_type_map = {
            "POWER_OE": ["홀", "짝"],
            "POWER_UO": ["언더", "오버"],
            "BASIC_OE": ["홀", "짝"],
            "BASIC_UO": ["언더", "오버"]
        }

        next_amount = MIN_AMOUNT
        print("check point 1")

        time.sleep(3)
        # tr_all = wait_selector_all(b, "#batlist tr", wait_time=30)
        # print("retrieve success tr")
        # for x in tr_all:
        #     print(x.text)
        # print("end tr")

        for tr in wait_selector_all(b, "#batlist tr", wait_time=30):
            title = tr.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text

            _type_info, _choice_info = title.split(" ")

            # print(f"title: {_type_info}, {_choice_info}")
            print(
                f"type match : {_type_info} == {type_result[_type]}, "
                f"choice in : {_choice_info} in {convert_type_map[_type]}"
            )
            if _type_info == type_result[_type] and _choice_info in convert_type_map[_type]:
                result_text = tr.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
                print(f"type is : {title}, result text: {result_text}")

                if result_text.__contains__("미적중"):
                    clean_amount = re.sub("\\D", "", tr.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text)
                    print(f"last amount: {clean_amount}")
                    next_amount = int((int(clean_amount) * 2.2) // 10 * 10)

                else:
                    next_amount = MIN_AMOUNT

                print(f"next amount: {next_amount}")
                break

        result = {
            "fiveType": _type,
            "choice": type_map[_type][type_idx[_type]],
            "amount": next_amount
        }
        type_idx[_type] += 1
        if type_idx[_type] > 12:
            type_idx[_type] = 0
        return result


    print(_id, cnt)

    view_mode = True
    options = Options()
    if not view_mode:
        options.add_argument('headless')

    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    options.add_argument('lang=ko_KR')
    b = webdriver.Chrome(options=options)
    cookie_dict = {}
    account_df = pd.read_csv('account.csv')
    _id, _pw, _url = account_df.iloc[0].id, account_df.iloc[0].pw, account_df.iloc[0].url
    b.get(_url)

    b.find_element(By.CSS_SELECTOR, "#userid").send_keys(_id)
    b.find_element(By.CSS_SELECTOR, "#userpw").send_keys(_pw)
    code = ""

    if not view_mode:
        b.save_screenshot('access_code.png')
        code = input("이미지에 보이는 보안 코드를 입력하세요: ")
        b.find_element(By.CSS_SELECTOR, ".codes").send_keys(code)
    else:
        b.find_element(By.CSS_SELECTOR, ".codes").send_keys(code)

    # b.implicitly_wait(15)
    time.sleep(17)

    try:
        b.switch_to.frame("live-iframe")
        sound = b.find_element(By.CSS_SELECTOR, "#btn_sound")
        b.execute_script("arguments[0].removeAttribute('on')", sound)
        b.switch_to.default_content()

        _cookies = b.get_cookies()

        for c in _cookies:
            cookie_dict[c['name']] = c['value']
            options.add_argument(f"{cookie_dict[c['name']]}={c['value']}")

        print(b.capabilities)
        print("init bat info", _id, _subnet)

        steps("POWER_OE")
        steps("POWER_UO")
        steps("BASIC_OE")
        steps("BASIC_UO")

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(e)
        print("exit exception")
    finally:
        b.close()
