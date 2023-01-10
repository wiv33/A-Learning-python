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
        self.is_mac = platform.platform().lower().__contains__('mac')
        self.driver = driver
        self._download()
        self._unzip()

    def _download(self):
        df = pd.read_csv('driver.csv')
        idx = 0 if self.is_mac else 1
        os.system(f'rm -f {self.driver}*.zip')
        wget.download(df.loc[idx].url)

    def _unzip(self):
        os.system(f'unzip {self.driver}*.zip')
        os.system(f'rm -f {self.driver}*.zip')


class Browser:
    def __init__(self, driver='chrome', view_mode=False):
        self._platform = _platform = platform.platform()
        self.driver = f'{driver}driver'
        self.view_mode = view_mode

        self.dp = user_path(self.driver) if self._platform.lower().__contains__('mac') else \
            user_path(f'{self.driver}.exe')
        self.setup_driver()

        self.options = webdriver.ChromeOptions()
        self.s = Service(self.dp)
        self.set_options()
        self.d = webdriver.Chrome(service=self.s, options=self.options)

    def setup_driver(self):
        print(f"{self._platform} # {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if not os.path.exists(self.dp):
            DriverDownloader(self.driver)

    def set_options(self, options=None):
        if options:
            self.options = options
            return

        if not self.view_mode:
            self.options.add_argument('headless')
        self.options.add_argument("--window-size=2000x1000")
        # self.options.add_argument('disable-gpu')
        self.options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                                  'like Gecko) Chrome/108.0.0.0 Whale/3.18.154.8 Safari/537.36')
        self.options.add_argument('lang=ko_KR')

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
    # return f"{os.getcwd()}/{file}"
    return f"{'/Users/auto/PycharmProjects/A-Learning-python/Crawling/_000_basic/_003_extract_number/'}/{file}"
