import copy
import datetime
import os
import platform
import re
import time
import base64

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class InitBrowser:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        platform_ = platform.platform()
        print(f"{platform_} # {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        dp = user_path('chromedriver')
        self.s = Service(dp)
        self.set_options()

    def set_options(self, options=None):
        if options:
            self.options = options
            return
        # self.options.add_argument('headless')
        self.options.add_argument("--window-size=1500x1000")
        # self.options.add_argument('disable-gpu')
        self.options.add_argument('user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ('
                                  'KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
        self.options.add_argument('lang=ko_KR')

    def create_browser(self):
        return webdriver.Chrome(service=self.s, options=self.options)


def user_path(last):
    return f"{os.getcwd()}/{last}"


def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


class DoorayLogin:
    def __init__(self, web_driver: WebDriver):
        self.driver = web_driver

        df = pd.read_csv(user_path('account_info.csv'))
        self.username, self.password = df.iloc[1]

    def login(self):
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, "#content > div > form > fieldset > div.input-wrap > div:nth-child(1) > "
                              "div > span > input[type=text]"))
        ).send_keys(self.username)
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#content > div > form > fieldset > div.input-wrap > div:nth-child(2) > '
                              'div > span > input[type=password]'))
        ).send_keys(self.password)

        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#content > div > form > fieldset > div.button-area > button > span'))
        ).click()


def select_element(web_driver, key):
    return WebDriverWait(web_driver, 5).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, key))
    )


class AddMember:
    def __init__(self):
        self.selector_btn = {
            "member_add_btn": "body > div.main > div.main-content > div > section > section > header > "
                              "div.d-row.row-align-center.header-buttons > button:nth-child(1)",
            "save_btn": "#d-modal-container > div > section > div > footer > div > button.eZWsHA.m.primary",
        }
        self.selector_field = {
            "name": "#d-modal-container > div > section > div > section > section > div > div:nth-child(2) > "
                    "div.d-col.col-content > div > div:nth-child(1) > input[type=text]",
            "nick_name": "#d-modal-container > div > section > div > section > section > div > div:nth-child(2) > "
                         "div.d-col.col-content > div > div.input-text-field.left-space-col.dDkHnX > input[type=text]",
            "id": "#d-modal-container > div > section > div > section > section > div > div:nth-child(3) > "
                  "div.d-col.col-content > div > input[type=text]",
            "password": "#d-modal-container > div > section > div > section > section > div > div:nth-child(4) > "
                        "div.d-col.col-content > div:nth-child(1) > div > input[type=password]",
            "password_check": "#d-modal-container > div > section > div > section > section > div > div:nth-child(4) > "
                              "div.d-col.col-content > div.d-row.row-direction-column.password-repeat-row > "
                              "div.input-text-field.dDkHnX > input[type=password]",
            "external_email": "#d-modal-container > div > section > div > section > section > div > "
                              "div.d-row.external-email-row > div.d-col.col-content > div > input[type=email]",
            "odm_base_date": "#d-modal-container > div > section > div > section > section > div > div:nth-child(12) > "
                             "div.d-col.col-content > div > div > div > input",
            "birthday": "#d-modal-container > div > section > div > section > section > div > "
                        "div.d-row.narrow-row.birthday-row > div.d-col.col-content > div > div.default-width > "
                        "div > div > input",

        }
        self.values_map = {
            "name": lambda n: n,
            "nick_name": lambda n: n,
            "id": 'dtest',
            "password": "nhn!@#123",
            "password_check": "nhn!@#123",
            "external_email": 'psawesome@nhnsoft.com',
            "odm_base_date": lambda date: date,
            "birthday": lambda date: date,
        }

        self.mapping = {
            "birthday": "odm_base_date",
        }

        self.df_user = pd.read_csv(user_path('annual_leave_user_list.csv'))
        if 'nick_name' not in self.df_user.columns:
            self.df_user['nick_name'] = self.df_user.apply(lambda x: f"{stringToBase64(x['tenant_nm'])}", axis=1)
            print(self.df_user.head())
            self.df_user.to_csv(user_path('annual_leave_user_list.csv'))

    def add(self, web_driver: WebDriver):
        for idx, x in enumerate(range(len(self.df_user))):
            self.btn_click(web_driver, 'member_add_btn')
            # tenant_id,name,organization_id,member_id,member_nm,odm_base_date,enter_date,sta_date,occur_num,use_num
            self.send_key(web_driver, 'name', idx)
            self.send_key(web_driver, 'id', idx)
            self.send_key(web_driver, 'nick_name', idx)
            self.send_key(web_driver, 'password', idx)
            self.send_key(web_driver, 'password_check', idx)
            self.send_key(web_driver, 'external_email', idx)
            self.send_key(web_driver, 'odm_base_date', idx)
            self.send_key(web_driver, 'birthday', idx)
            self.btn_click(web_driver, 'save_btn')

    def btn_click(self, web_driver, btn_key):
        select_element(web_driver, self.selector_btn[btn_key]).click()

    def send_key(self, web_driver, element_key, idx):
        temp_key = copy.deepcopy(element_key)
        if element_key in self.mapping:
            temp_key = self.mapping[element_key]

        value = ''
        if isinstance(self.values_map[temp_key], str):
            value = (self.values_map[temp_key])
            if temp_key == 'id':
                value = value + (str(idx) if idx > 9 else f'0{idx}')
        else:
            value = (self.values_map[temp_key](self.df_user.loc[idx, [temp_key]]))

        select_element(web_driver, self.selector_field[element_key]).send_keys(value)


if __name__ == '__main__':
    d = InitBrowser().create_browser()
    try:
        url = 'https://psa.beta.dooray.com/org/department-member?orgFilter=psa'
        d.get(url)
        DoorayLogin(d).login()
        time.sleep(2)
        AddMember().add(d)
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        d.quit()
