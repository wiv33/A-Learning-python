import datetime
import json
import re
import time
import schedule

import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WebController:
    def __init__(self, view_mode=True):
        options = Options()
        if not view_mode:
            options.add_argument('headless')

        options.add_argument("--window-size=1920,1080")
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                             'like Gecko)Chrome/109.0.0.0 Safari/537.36')
        options.add_argument('lang=ko_KR')
        self.d = webdriver.Chrome(options=options)

    def waiting(self, selector):
        _cnt = 0
        while True:
            try:
                print(f"check available time ... {_cnt}")
                starting_time = self.select_wait(selector, timeout=30)
                sub_text = re.sub('\\D', "", starting_time.text)
                if sub_text and int(sub_text) > 50:
                    break
                time.sleep(10)
                _cnt += 10
            except Exception as _e:
                _cnt += 10
                print(f"starting is not available retry seconds {_cnt}...", _e.__str__())
        print("start next batting ...")

    def required_selector(self, required_select_func):
        _ele = None
        while True:
            while _ele is None:
                try:
                    _ele = required_select_func(self)
                    time.sleep(1)
                except Exception as __e:
                    time.sleep(1)

            return _ele

    def select_wait(self, selector, timeout=5, by=By.CSS_SELECTOR):
        return WebDriverWait(self.d, timeout).until((
            ec.presence_of_element_located(
                (by, selector)
            )
        ))

    def select_all_wait(self, selector, wait_time=5, by=By.CSS_SELECTOR):
        return WebDriverWait(self.d, wait_time).until((
            ec.presence_of_all_elements_located(
                (by, selector)
            )
        ))
