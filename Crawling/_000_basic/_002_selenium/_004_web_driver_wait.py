from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver

import _003_daum_news_by_service


def runner(d: WebDriver):
    hidden_submenu = d.find_element(By.CLASS_NAME, '.nav #submenu1')
    actions = webdriver.ActionChains(d)
    actions.click(hidden_submenu)
    actions.perform()


if __name__ == '__main__':
    deco = _003_daum_news_by_service.BrowserDecorator()
    deco.run_browser('https://news.v.daum.net/v/20170202185812986', runner)
