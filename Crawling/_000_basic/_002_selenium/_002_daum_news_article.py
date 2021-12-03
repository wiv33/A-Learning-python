from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = '/usr/local/bin/chromedriver'
# 1.
# d = webdriver.Chrome(chromedriver)

# 2.
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                     'like Gecko) Chrome/96.0.4664.55 Safari/537.36')
options.add_argument('lang=ko_KR')

d = webdriver.Chrome(driver_path, options=options)
d.get('https://news.v.daum.net/v/20170202185812986')

# title_list = d.find_elements(By.TAG_NAME, 'h3')
title = d.find_element(By.CSS_SELECTOR, 'h3.tit_view')
# head_title = title.find_element(By.CSS_SELECTOR, 'html head')
# print(head_title.get_attribute('text'), " : ", head_title.text)
print(title.get_attribute('text'), " : ", title.text)


d.quit()

