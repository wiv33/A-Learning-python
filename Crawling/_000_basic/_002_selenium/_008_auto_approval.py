import datetime
import os
import platform
import re
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class AutoApproval:
    """
    crontab # 0,17,37,57 * * * * PATH=/usr/local/bin python /Users/nhn/PycharmProjects/A-Learning-python/Crawling/_000_basic/_002_selenium/_008_auto_approval.py
    pyinstaller --onefile(-F) --name(-n) auto_approval /Users/nhn/PycharmProjects/A-Learning-python/Crawling/_000_basic/_002_selenium/_008_auto_approval.py # --target-arch x86_64
    crontab # 7,39 * * * * 7,39 * * * * /Users/nhn/dist/auto_approval >> /Users/nhn/dist/auto_approval.log 2>&1
    """

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        platform_ = platform.platform()
        dp = user_path('chromedriver.exe')
        print(f"{platform_} # {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if platform_.lower().__contains__('mac'):
            dp = user_path('chromedriver')
        self.s = Service(dp)
        self.set_options()

    def set_options(self, options=None):
        if options:
            self.options = options
            return
        self.options.add_argument('headless')
        self.options.add_argument("--window-size=1500x1000")
        # self.options.add_argument('disable-gpu')
        self.options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                                  'like Gecko) Chrome/108.0.0.0 Whale/3.18.154.8 Safari/537.36')
        self.options.add_argument('lang=ko_KR')

    def create_browser(self):
        return webdriver.Chrome(service=self.s, options=self.options)


def user_path(last):
    return f"{os.getcwd()}/{last}"


if __name__ == '__main__':
    a = AutoApproval()
    d = a.create_browser()
    url = 'https://nhnent.dooray.com/mail/systems/inbox'

    complete_cnt = 0
    try:
        df = pd.read_csv(user_path('account_info.csv'))
        username, password = df.iloc[0]

        d.get(url)
        time.sleep(1)

        d.find_element(By.ID, 'username').send_keys(username)
        d.find_element(By.ID, 'password').send_keys(password)
        time.sleep(3)

        WebDriverWait(d, 5).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '.btn.btn-submit.btn-block'))
        ).click()
        time.sleep(5)

        if re.search('<span class="ng-scope">서비스에 접근할 수 없습니다.</span>', d.page_source):
            raise Exception(f"failed SAP connection # {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        c = '결재_자동_승인'
        category = WebDriverWait(d, 5).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, f'mail-navi-user-folders.ng-scope > ul:nth-child(2) a[title="{c}"]')))

        if not category:
            raise Exception(f'`{c}` 카테고리가 없습니다.')

        WebDriverWait(d, 5).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="main-wrapper"]/section/mail-body-container/div/mail-navi/section/div/div'
                       '/ng-transclude/mail-navi-user-folders/ul/li[3]/div[1]/div/div/div/a'))
        ).click()

        time.sleep(2)
        elements = d.find_elements(By.CSS_SELECTOR, '.ng-scope.ng-isolate-scope.unread')
        for x in elements:
            if not x.text.startswith('결재'):
                break
            x.click()
            WebDriverWait(d, 5).until(ec.presence_of_element_located((By.XPATH,
                                                                      '//*[@id="mailContentsView-subject-anchor"]/section/div[3]/div/div/div/div/div[4]/table/tbody/tr/td/a/span'))).click()
            time.sleep(3)

            d.switch_to.window(d.window_handles.__getitem__(1))
            try:
                if WebDriverWait(d, 4).until(
                        ec.element_to_be_clickable((By.CSS_SELECTOR, '#devUserButtonLeft.section_last > a.btn.green'))):
                    btn = WebDriverWait(d, 5).until(
                        ec.presence_of_element_located(
                            (By.CSS_SELECTOR, '#devUserButtonLeft.section_last > a.btn.green')))
                    if btn:
                        complete_cnt += 1
                        btn.click()
                    else:
                        d.close()
                        continue
            except Exception as e:
                print(e)
                d.close()
                d.switch_to.window(d.window_handles.__getitem__(0))
                continue

            time.sleep(1)

            d.close()
            d.switch_to.window(d.window_handles.__getitem__(0))

    except Exception as err:
        print(err)
    finally:
        if complete_cnt > 0:
            print(f"complete: {complete_cnt}, # {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        d.quit()
