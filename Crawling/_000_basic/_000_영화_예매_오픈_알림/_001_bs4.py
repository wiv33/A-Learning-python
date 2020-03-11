"""bs4
BeautifulSoup 객체
select() 메서드 활용
"""
import requests
from bs4 import BeautifulSoup

url = "https://cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200326"
html = requests.api.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('.info-movie')
for item in title_list:
    # text.strip() -> trim()
    print(item.select_one("a > strong").text.strip())

