import datetime
import os
import platform
import random
import urllib.request
import wget
import sys

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DriverDownloader:
    def __init__(self):
        self.is_mac = platform.platform().lower().__contains__('mac')
        self._download()
        self._unzip()

    def _download(self):
        df = pd.read_csv('driver.csv')
        idx = 0 if self.is_mac else 1
        os.system("rm -f chromedriver*.zip")
        wget.download(df.loc[idx].url)

    def _unzip(self):
        os.system('unzip chromedriver*.zip')
        os.system("rm -f chromedriver*.zip")


class GBBrowser:
    def __init__(self):
        _platform = platform.platform()
        dp = user_path('chromedriver') if _platform.lower().__contains__('mac') else user_path('chromedriver.exe')
        print(f"{_platform} # {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if not os.path.exists(dp):
            DriverDownloader()
            # raise ValueError("not exists driver")

        self.options = webdriver.ChromeOptions()
        self.s = Service(dp)
        self.set_options()
        self.d = webdriver.Chrome(service=self.s, options=self.options)

    def set_options(self, options=None):
        if options:
            self.options = options
            return
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


def user_path(file):
    return f"{os.getcwd()}/{file}"


if __name__ == '__main__':
    gb = GBBrowser()
    d = gb.driver()
    try:
        pd_read_gb = pd.read_csv('gb_url.csv')
        url = pd_read_gb.iloc[0].url
        d.get(url)

        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                                       'like Gecko) Chrome/108.0.0.0 Whale/3.18.154.8 Safari/537.36')
        opener.addheader('Referer', url)
        opener.addheader('Host', pd_read_gb.iloc[0].host)
        opener.addheader('Cookie',
                         f'PHPSESSID={d.get_cookie("PHPSESSID").get("value")}; idCookies=sun19%7Csun18; VisitCookie=211.230.202.69')
        gb.wait_selector('.login_wrapper.pc > a').click()
        kaptcha_img = gb.wait_selector('kcaptcha_image', by=By.ID)
        kaptcha_img.get_attribute("src")

        opener.retrieve(kaptcha_img.get_attribute("src"),
                        f"./sample/train_four_numbers/unknown_{random.choice(range(30000, 77777))}.jpeg")
    except Exception as err:
        print(err)
    d.quit()
