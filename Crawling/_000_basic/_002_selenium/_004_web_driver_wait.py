from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import _003_daum_news_by_service


def runner_04(d: WebDriver):
    loop, count = True, 0

    while loop and count < 10:
        try:
            tag_selector = '#alex-area > div > div > div > div.cmt_box > div.alex_more > button'
            element = WebDriverWait(d, 5).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, tag_selector))
            )
            more_btn = d.find_element(By.CSS_SELECTOR, tag_selector)
            webdriver.ActionChains(d).click(more_btn).perform()
            count += 1
            time.sleep(2)
        except TimeoutException:
            loop = False

    comment_box = d.find_element(By.CSS_SELECTOR, '#alex-area > div > div > div > div.cmt_box > ul.list_comment')
    comment_list = comment_box.find_elements(By.TAG_NAME, 'li')
    for i, x in enumerate(comment_list):
        print(f"[{i}] {x.find_element(By.CSS_SELECTOR, 'div p').text}")

    d.quit()


if __name__ == '__main__':
    deco = _003_daum_news_by_service.BrowserDecorator()
    deco.run_browser('https://news.v.daum.net/v/20170202185812986', runner_04, True)
