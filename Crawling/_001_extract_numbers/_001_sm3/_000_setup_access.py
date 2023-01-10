import os
import random
import time
import urllib.request

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from concurrent.futures import ProcessPoolExecutor

from Crawling._001_extract_numbers._001_sm3.BrowserModule import Browser


def user_path(file):
    return f"{os.getcwd()}/{file}"


def download_kaptcha(idx):
    try:
        b = Browser(view_mode=False)
        d = b.d
        url_info_df = pd.read_csv(user_path("gb_url.csv"))
        info_df = url_info_df.iloc[0]

        url = info_df.access_url

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
        for _ in range(1000):
            kaptcha_img = d.find_element(By.CSS_SELECTOR, info_df.img_selector)
            opener.retrieve(kaptcha_img.get_attribute("src"),
                            f"./model/unknown/zzz_{idx}_change_me_{random.choice(range(777777))}.png")
            d.find_element(By.TAG_NAME, 'body').send_keys(Keys.F5)
        d.quit()

    except Exception as err:
        print(err)


if __name__ == '__main__':
    PRIMES = np.arange(40)
    with ProcessPoolExecutor(max_workers=20) as e:
        e.map(download_kaptcha, PRIMES)

