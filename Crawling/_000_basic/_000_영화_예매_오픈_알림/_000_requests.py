import requests
from bs4 import BeautifulSoup

url = "https://cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200226"
api = requests.api.get(url)

print(api.text)
