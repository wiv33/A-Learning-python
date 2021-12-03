from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time
import _003_daum_news_by_service


def runner_05(d: WebDriver):
    user_name =
    pass


if __name__ == '__main__':
    deco = _003_daum_news_by_service.BrowserDecorator()
    deco.run_browser('https://www.facebook.com/', runner_05, True)
