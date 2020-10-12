from bs4 import BeautifulSoup, builder
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
import pandas as pd
import re

from selenium import webdriver

from wordcloud import WordCloud
from collections import Counter
import collections

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# wd = webdriver.Chrome('chromedriver')
# driver = webdriver.Chrome('chromedriver')


class TakeArticle:
    def __init__(self):
        """
        df_docs
            테이블 형식의 데이터 프레임 생성
        current_date
            오늘 날짜부터 limit_day 전 기사를 가져오기 위한 파라미터
        limit_day
            오늘부터 추출할 날짜
        wd
            webdirver

        wc
            WordCloud 이미지 생성을 위한 객체
        """
        self.df_docs = pd.DataFrame(columns=['title', 'body'])
        self.current_date = datetime.datetime.now().date()
        self.limit_day = datetime.datetime.today() - datetime.timedelta(days=30)
        self.wd = webdriver.Chrome('chromedriver')
        self.wc = WordCloud(
            width=800,
            height=800,
            background_color='white'
        )

    def add_more_of_article_list(self):
        """ more 버튼 눌러서 기사 모으기 """
        self.wd.get('https://koreajoongangdaily.joins.com/section/allArticles')

        print(self.limit_day.date())
        final_article = datetime.datetime.now().date()
        # 각 기사의 url을 가져온다.
        cnt = 10
        while self.limit_day.date().__lt__(final_article):
            # print(self.limit_day.date().__lt__(final_article))
            final_article = datetime.datetime.fromisoformat(self.wd.find_element_by_css_selector(  # required python by 3.8.6
            # final_article = datetime.datetime.strptime(self.wd.find_element_by_css_selector(
                '#main-second-content > div.article-left > div:nth-child(%d) > a > span.media-date > span' % cnt).text).date()
            # print(final_article)
            self.wd.find_element_by_class_name('service-more-btn').click()
            # wd.find_element_by_xpath('//*[@id="article_more"]/button').click()
            time.sleep(1)
            cnt += 10

    def make_docs(self):
        """ 모은 기사 url을 기반으로 DataFrame 내용 채우기 """
        a_list = self.wd.find_elements_by_xpath('//*[@id="main-second-content"]/div[1]/div[*]/a')
        print("a list size is {}".format(len(a_list)))
        for a in a_list:
            # print(a)
            # print('href is {}'.format(a.get_attribute('href')))
            article = requests.get(a.get_attribute('href'))
            soup = BeautifulSoup(article.text, builder.HTML)
            body = soup.select_one('#article_body')
            title = body.select_one(".view-article-title.serif")
            print('title :: {}'.format(title.get_text()))
            body_text = body.get_text().replace(title.get_text(), "")
            self.df_docs = self.df_docs.append({'title': title.get_text(), 'body': body_text}, ignore_index=True)

    def make_csv(self):
        """ csv 파일로 변환하기 """
        self.df_docs.to_csv("recent_month_popular_{}.csv".format(self.current_date))

    def clean_text(self, txt: str) -> str:
        """기사 본문에 있는 특수문자 제거하기 """
        return re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》\\n\xa0]', '', txt)

    def word_cloud(self):
        words = self.df_docs.iloc[:, 3].values.flatten()
        result = dict(Counter(words).most_common(100))
        self.wc.generate_from_frequencies(result)

    def make_word_cloud(self):
        self.wc.to_image()


article = TakeArticle()
article.add_more_of_article_list()
article.make_docs()
article.df_docs['cleanBody'] = article.df_docs['body'].apply(article.clean_text)
article.make_csv()
