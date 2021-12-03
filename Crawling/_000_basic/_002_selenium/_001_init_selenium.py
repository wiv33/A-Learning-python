from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/usr/local/bin/chromedriver'
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

d = webdriver.Chrome(chromedriver, options=options)


# phantomJS deprecate

d.get("http://www.python.org/")
print(d.title)
print(d.current_url)

assert "Python" in d.title

search = d.find_element(By.ID, 'id-search-field')
search.clear()
search.send_keys('python')
search.send_keys(Keys.ENTER)

assert 'No results found.' not in d.page_source

data = d.find_elements(By.CSS_SELECTOR, '#content > div > section > form > ul > li > h3 > a')
for item in data:
    print(item.text)

time.sleep(7)
d.quit()
