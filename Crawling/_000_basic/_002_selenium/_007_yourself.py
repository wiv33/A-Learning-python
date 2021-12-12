from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

from selenium.webdriver.support.wait import WebDriverWait


def init_service():
    dp = '/usr/local/bin/chromedriver'
    return Service(dp)


def init_options():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('disable-gpu')
    options.add_argument('user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/96.0.4664.52 Whale/3.12.129.29 Safari/537.36')
    options.add_argument('lang=ko_KR')
    options.add_argument('Cookie: WAF=a80222f7dca55f12978d17b23cbc44c5; _'
                         'JSESSIONID=0156DA8A6EEA102976B3EC0636D1BBE9229CC5F562D3CC4290BCD0E46D8E9B5AF7BFB63ACCCF33253CFC5DB031E7EF1144AC4F81AC64')
    return options


def yourself_access(d: WebDriver):
    school = d.find_element(By.CSS_SELECTOR, '.type1')
    school.click()

    el = d.find_element(By.ID, 'btnConfirm2')
    el.click()


def login_yourself(d: WebDriver, df: DataFrame, idx: int):
    # 학교 설정
    school = d.find_element(By.ID, 'schul_name_input')
    school.click()

    city = Select(d.find_element(By.ID, 'sidolabel'))
    city.select_by_index(1)

    level = Select(d.find_element(By.ID, 'crseScCode'))
    level.select_by_index(2)

    org = d.find_element(By.ID, 'orgname')
    school_name = df.loc[idx, 'orgName']
    org.send_keys(school_name)

    search = d.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button/span')
    search.click()

    element = WebDriverWait(d, 2).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a')))
    element.click()

    d.find_element(By.CSS_SELECTOR, '#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input').click()

    # 이름
    name = df.loc[idx, 'userName']
    d.find_element(By.ID, 'user_name_input').send_keys(name)

    # 생년월일
    d.find_element(By.ID, 'birthday_input').send_keys(100625)
    d.find_element(By.ID, 'btnConfirm').click()

    password(d, df.loc[idx, 'password'])


def password(d: WebDriver, pass_arr: []):
    WebDriverWait(d, 2).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#password'))).click()
    # d.find_element(By.CSS_SELECTOR, '#password').click()
    time.sleep(2)

    for x in pass_arr:
        d.find_element(By.CSS_SELECTOR, "a[class^=transkey_div][aria-label='{}']".format(x)).click()

    d.find_element(By.ID, 'btnConfirm').click()


def start_yourself(d: WebDriver, child):
    time.sleep(1)
    d.find_element(By.CSS_SELECTOR, f'#container .memberWrap div li:nth-child({child}) em').click()

    time.sleep(1)
    for x in range(1, 5):
        d.find_element(By.ID, f'survey_q{x}a1').click()

    time.sleep(1)
    d.find_element(By.ID, 'btnConfirm').click()
    d.find_element(By.XPATH, '/html/body/app-root/div/div[1]/div[1]/ul/li/a/span').click()


def run_crawl():
    df = pd.read_json('db_info.json', 'r')
    print(df.loc[0, 'password'])
    print(df.loc[0, 'orgName'])
    print(df.loc[0, 'userName'])
    print(df.loc[0, 'birth'])
    s = init_service()
    d = webdriver.Chrome(service=s, options=init_options())

    try:
        d.get('https://hcs.eduro.go.kr')
        yourself_access(d)
        login_yourself(d, df, idx=0)
        time.sleep(1)
        start_yourself(d, 1)
        start_yourself(d, 2)
        time.sleep(7)
    except Exception as err:
        print(err)
        d.quit()

    d.quit()
    pass


if __name__ == '__main__':
    run_crawl()
    pass
