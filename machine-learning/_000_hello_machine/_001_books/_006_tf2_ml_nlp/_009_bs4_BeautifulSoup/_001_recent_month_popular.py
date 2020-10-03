from bs4 import BeautifulSoup, builder
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
import pandas as pd

browser = webdriver.Chrome('chromedriver.exe')
# browser.maximize_window()  # 창을 최대로

browser.get('https://koreajoongangdaily.joins.com/section/allArticles')

df_docs = pd.DataFrame(columns=['title', 'body'])
# 각 기사의 url을 가져온다.
a_list = []
current_date = datetime.datetime.now().date()
is_ge_month = datetime.datetime.now().date()
#  TODO 계속 클릭해서 more를 늘린다.
while current_date.__ge__(is_ge_month):
    a_list.append(browser.find_elements_by_xpath('//*[@id="main-second-content"]/div[*]/div[*]/a'))

# print(a_list, end='\n\n')
for a in a_list:
    # print('href is {}'.format(a.get_attribute('href')))
    article = requests.get(a.get_attribute('href'))
    soup = BeautifulSoup(article.text, builder.HTML)
    body = soup.select_one('#article_body')
    title = body.select_one(".view-article-title.serif")
    print('title :: {}'.format(title.get_text()))
    body_text = body.get_text().replace(title.get_text(), "")
    df_docs = df_docs.append({'title': title, 'body': body_text}, ignore_index=True)


print(df_docs.head())
browser.close()