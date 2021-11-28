from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://python.org')

print(driver.title)
assert 'Python' in driver.title

elem = driver.find_element(By.NAME, 'q')
elem.clear()

elem.send_keys('python')
elem.send_keys(Keys.RETURN)

assert 'No results found.' not in driver.page_source

time.sleep(10)
driver.quit()
