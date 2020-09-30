from bs4 import BeautifulSoup

string = '<body>gogogogogo <br/> <br/></body>'
soup = BeautifulSoup(string, "lxml")

string = soup.get_text()
print(string)
# gogogogogo