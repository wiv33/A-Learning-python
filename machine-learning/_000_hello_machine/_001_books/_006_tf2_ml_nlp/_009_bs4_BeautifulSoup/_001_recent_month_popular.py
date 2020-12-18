from bs4 import BeautifulSoup, builder
import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
import pandas as pd

wd = webdriver.Chrome('chromedriver.exe')
wd.maximize_window()  # 창을 최대로

wd.get('https://koreajoongangdaily.joins.com/section/allArticles')

df_docs = pd.DataFrame(columns=['title', 'body'])
# 각 기사의 url을 가져온다.
current_date = datetime.datetime.now().date()
limit_month = datetime.datetime.today() - datetime.timedelta(days=30)
print(limit_month)
final_article = datetime.datetime.now().date()
cnt = 10
while limit_month.date().__lt__(final_article):
    print(limit_month.date().__lt__(final_article))
    # final_article = datetime.datetime.fromisoformat(wd.find_element_by_css_selector(  # required python by 3.8.6
    final_article = datetime.datetime.strptime(wd.find_element_by_css_selector(
        '#main-second-content > div.article-left > div:nth-child(%d) > a > span.media-date > span' % cnt).text,
                                               '%Y-%m-%d').date()
    print(final_article)
    wd.find_element_by_class_name('service-more-btn').click()
    # wd.find_element_by_xpath('//*[@id="article_more"]/button').click()
    time.sleep(1)
    cnt += 10

a_list = wd.find_elements_by_xpath('//*[@id="main-second-content"]/div[1]/div[*]/a')
print(a_list, end='\n\n')
for a in a_list:
    print(a)
    print('href is {}'.format(a.get_attribute('href')))
    article = requests.get(a.get_attribute('href'))
    soup = BeautifulSoup(article.text, builder.HTML)
    body = soup.select_one('#article_body')
    title = body.select_one(".view-article-title.serif")
    print('title :: {}'.format(title.get_text()))
    body_text = body.get_text().replace(title.get_text(), "")
    df_docs = df_docs.append({'title': title.get_text(), 'body': body_text}, ignore_index=True)

print(df_docs.head())
df_docs.to_csv("recent_month_popular_{}.csv".format(current_date))
wd.quit()

#  TODO 텍스트 데이터 전처리 시작
# 최근 한 달 기사
# 1. 주요 키워드 CounterVectorized
# 2. 핵심 키워드 Tf-idf
