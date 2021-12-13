import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
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

    element = WebDriverWait(d, 3).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a')))
    element.click()

    d.find_element(By.CSS_SELECTOR, '#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input').click()

    # 이름
    name = df.loc[idx, 'userName']
    d.find_element(By.ID, 'user_name_input').send_keys(name)

    # 생년월일
    d.find_element(By.ID, 'birthday_input').send_keys(df.loc[idx, 'birth'])
    d.find_element(By.ID, 'btnConfirm').click()

    password(d, df.loc[idx, 'password'])


def password(d: WebDriver, pass_arr: []):
    WebDriverWait(d, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#password'))).click()
    # d.find_element(By.CSS_SELECTOR, '#password').click()
    time.sleep(3)

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
    s = init_service()
    d = webdriver.Chrome(service=s, options=init_options())

    try:
        d.get('https://hcs.eduro.go.kr')
        yourself_access(d)
        login_yourself(d, df, idx=0)
        time.sleep(1)
        start_yourself(d, 1)
        start_yourself(d, 2)
        send_mail("covid-19 school is done")
        time.sleep(7)
    except Exception as errObj:
        print(errObj)
        send_mail(errObj.__str__())
        d.quit()

    d.quit()


def send_mail(subject):
    df = pd.read_csv('mail_info.csv')
    sender_email, receiver_email, pw, success, fail = df.loc[0]

    print(sender_email, receiver_email, pw)

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
    html = f"""\
        <html>
          <body>
            {success if subject.startswith('covid-19') else fail}
          </body>
        </html>
        """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, pw)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


if __name__ == '__main__':
    try:
        run_crawl()
    except Exception as err:
        print(err)
