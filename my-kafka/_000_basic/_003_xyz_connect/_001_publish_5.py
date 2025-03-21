import json

import selenium.webdriver.chromium.webdriver

from _000_KafkaManager import KafkaManager, PB_TOPIC_5, PB_TOPIC_5_TEST
import datetime
import os
import platform
import wget

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DriverDownloader:
    def __init__(self, driver='chromedriver'):
        self._platform = platform.system().lower()
        print(self._platform)
        self.driver = driver
        self._download()
        self._unzip()

    def _download(self):
        df = pd.read_csv(user_path('driver.csv'), index_col='keys')
        print("download : ", df)
        os.system(f'rm -f {self.driver}*.zip')
        wget.download(df.loc[self._platform].url)

    def _unzip(self):
        os.system(f'unzip {self.driver}*.zip')
        os.system("chmod +x chromedriver")
        os.system("mv chromedriver /usr/local/share/chromedriver")
        os.system("ln -s /usr/local/share/chromedriver /usr/src/chromedriver")
        print(os.system("which chromedriver"))
        print(os.system("chromedriver --version"))
        os.system(f'rm -f {self.driver}*.zip')


class Browser:
    def __init__(self, driver='chrome', view_mode=False):
        self._platform = _platform = platform.system().lower()
        self.driver = f'{driver}driver'
        self.view_mode = view_mode

        self.dp = user_path(f'{self.driver}.exe') if self._platform.__contains__('windows') else \
            user_path(self.driver)

        print("service dp: %s" % self.dp)
        self.setup_driver()

        self.options = webdriver.ChromeOptions()
        print("chrome/chromedriver version check")
        os.system("/usr/src/chrome/chromedriver --version")
        print("chromedriver exists : ", os.path.exists("./chrome/chromedriver"))

        self.s = Service(self.dp)
        self.set_options()
        self.d = webdriver.Chrome(service=self.s, options=self.options)

    def setup_driver(self):
        print(f"{platform.platform()} # {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if not os.path.exists("/usr/src/chrome/chromedriver"):
            DriverDownloader(self.driver)

    def set_options(self, options=None):
        if options:
            self.options = options
            return

        if not self.view_mode:
            self.options.add_argument('headless')
        # self.options.add_argument("--window-size=2000x1000")
        # self.options.add_argument('disable-gpu')
        self.options.add_argument(
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Whale/3.18.154.8 Safari/537.36')
        self.options.add_argument('lang=ko_KR')
        if self._platform.lower().__contains__("linux"):
            print("set no sandbox")
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--disable-dev-shm-usage')

        print(self.options.arguments)

    def driver(self):
        return self.d

    def wait_selector(self, selector, wait_time=5, by=By.CSS_SELECTOR):
        return WebDriverWait(self.d, wait_time).until((
            ec.presence_of_element_located(
                (by, selector)
            )
        ))

    def wait_selector_all(self, selector, wait_time=5, by=By.CSS_SELECTOR):
        return WebDriverWait(self.d, wait_time).until((
            ec.presence_of_all_elements_located(
                (by, selector)
            )
        ))

    def new_tab(self):
        self.d.execute_script('')

    def login(self, login_script):
        login_script(self)


def user_path(file):
    print(f"current path : {os.getcwd()}")
    # return f"{os.getcwd()  if '/' !=  os.getcwd() else ''}/{file}"
    return f"{'/Users/auto/PycharmProjects/A-Learning-python/my-kafka/_000_basic/_003_xyz_connect'}/{file}"


if __name__ == '__main__':
    service = Browser()
    service.d.get("https://ntry.com/scores/eos_powerball/main.php?game_type=5")
    last_data = service.wait_selector_all("#round-history tr:nth-child(1) td", wait_time=30)
    # 12
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    algo, result, section, odd_even, under_over, \
        num_result, num_sum, num_section, num_size, num_odd_even, num_under_over = last_data

    msg = {
        "date": date,
        "algo": algo.text,
        "powerBall": {
            "result": result.text,
            "section": section.text,
            "odd_even": odd_even.text,
            "under_over": under_over.text,
        },
        "basicBall": {
            "result": num_result.text,
            "sum": num_sum.text,
            "section": num_section.text,
            "size": num_size.text,
            "odd_even": num_odd_even.text,
            "under_over": num_under_over.text,
        }
    }

    msg_2 = {
        "date": date,
        "algo": algo.text,
        "power_result": result.text,
        "power_section": section.text,
        "power_odd_even": odd_even.text,
        "power_under_over": under_over.text,
        "basic_result": num_result.text,
        "basic_sum": num_sum.text,
        "basic_section": num_section.text,
        "basic_size": num_size.text,
        "basic_odd_even": num_odd_even.text,
        "basic_under_over": num_under_over.text,
    }

    KafkaManager().publish_message(PB_TOPIC_5, msg_2, 'p5')
    KafkaManager().publish_message(PB_TOPIC_5_TEST, msg, 'p5')

# def requests_test():
#     import requests
#     from bs4 import BeautifulSoup
#
#     url = "https://ntry.com/scores/eos_powerball/main.php?game_type=5"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/50.0.2661.102 Safari/537.36'}
#     html = requests.get(url, headers=headers)
#     print(html)
#
#     soup = BeautifulSoup(html.text, 'html.parser')
#     history_info = soup.select('.powerball_stats_list')
#
#     print(history_info)
