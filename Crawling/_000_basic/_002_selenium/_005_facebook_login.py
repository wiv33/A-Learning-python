from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time
import _003_daum_news_by_service


def runner_05(d: WebDriver):
    username = 'my account id'
    password = 'my password'
    username_id = '//*[@id="email"]'
    password_id = '//*[@id="pass"]'
    login_btn = '//*[@name="login"]'
    username_tag = WebDriverWait(d, 5).until(ec.presence_of_element_located((By.XPATH, username_id)))
    password_tag = WebDriverWait(d, 5).until(ec.presence_of_element_located((By.XPATH, password_id)))
    login_btn_tag = WebDriverWait(d, 5).until(ec.presence_of_element_located((By.XPATH, login_btn)))

    username_tag.clear()
    username_tag.send_keys(username)
    time.sleep(1)
    password_tag.clear()
    password_tag.send_keys(password)
    time.sleep(1)

    assert login_btn_tag is not None
    login_btn_tag.click()


if __name__ == '__main__':
    deco = _003_daum_news_by_service.BrowserDecorator()
    deco.run_browser('https://www.facebook.com/', runner_05)
