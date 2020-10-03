from bs4 import BeautifulSoup, builder
import datetime

string = '<body>gogogogogo <br/> <br/></body>'
soup = BeautifulSoup(string, builder.HTML)

string = soup.get_text()
print(string)
# gogogogogo


print(datetime.datetime.now().date().__ge__(datetime.datetime.fromisoformat('2020-09-10')))

limit_month = datetime.datetime.today() - datetime.timedelta(days=30)
print(limit_month.date())


