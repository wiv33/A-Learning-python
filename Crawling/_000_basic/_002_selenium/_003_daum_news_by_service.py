from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BrowserDecorator:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver_path = '/usr/local/bin/chromedriver'
        self.s = Service(self.driver_path)

    def init_driver(self, headers=None):
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1920x1080')
        self.options.add_argument('disable-gpu')
        self.options.add_argument(
            'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/96.0.4664.55 Safari/537.36')
        self.options.add_argument('lang=ko_KR')

    def run_browser(self, url, func, active_headless=False):
        if active_headless:
            self.init_driver()
        d = webdriver.Chrome(service=self.s, options=self.options)
        d.get(url=url)
        try:
            func(d)
        except Exception:
            d.quit()
        time.sleep(2)
        d.quit()


def run_func(d: WebDriver):
    print("is run?")
    elements = d.find_elements(By.TAG_NAME, 'a')
    for x in elements:
        print(x.text)


if __name__ == '__main__':
    deco = BrowserDecorator()
    deco.init_driver()
    deco.run_browser('https://news.v.daum.net/v/20170202185812986', run_func)
