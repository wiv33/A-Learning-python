import os.path
import re
import time
import urllib.request

import pandas as pd
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Crawling._001_extract_numbers._001_sm3.BrowserModule import Browser, user_path
from Crawling._001_extract_numbers._001_sm3._001_setup_train_6_numbers import CaptchaModelSix

service = Browser(view_mode=True)
d = service.d
all_info_df = pd.read_csv(user_path("./gb_url.csv"))
all_account_df = pd.read_csv(user_path("./account.csv"))
info_df = all_info_df.iloc[0]
account_df = all_account_df.iloc[0]
url = info_df.access_url


def get_captcha_img():
    d.get(url)

    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 '
                                   'Firefox/108.0')
    opener.addheader('Referer', url)
    opener.addheader('Host', info_df.host)
    get = d.get_cookie("PHPSESSID").get("value")
    print(get)
    opener.addheader('Cookie',
                     f'PHPSESSID={get}')
    kaptcha_img = d.find_element(By.CSS_SELECTOR, info_df.img_selector)
    opener.retrieve(kaptcha_img.get_attribute("src"),
                    "delete_me.png")
    return "delete_me.png"


def login():
    captcha_model = CaptchaModelSix()

    d.get(info_df.access_url)

    while True:
        img = get_captcha_img()
        _result = captcha_model.predict(img)
        print(_result)
        if len(re.sub("[^0-9]", "", _result)) == 6:
            break

    print(_result)
    service.wait_selector("#userid").send_keys(account_df.id)
    service.wait_selector("#userpw").send_keys(account_df.pw)
    service.wait_selector(".codes").send_keys(_result)
    service.wait_selector(".btn_login > span:nth-child(1)").click()
    time.sleep(1)

    # d.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)
    # time.sleep(1)

    if os.path.exists('delete_me.png'):
        os.system("rm -f delete_me.png")


if __name__ == '__main__':
    login()
