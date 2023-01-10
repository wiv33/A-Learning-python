import random
import time

from selenium.webdriver.common.by import By

from BrowserModule import Browser, user_path
import pandas as pd

if __name__ == '__main__':
    MINIMUM_AMOUNT = 100


    def login_sbuks(_service):
        account_df = pd.read_csv('account.csv')
        _service.wait_selector("#username").send_keys(account_df.iloc[0].username)
        _service.wait_selector("#password").send_keys(account_df.iloc[0].password)
        _service.wait_selector(".btn_login").click()


    service = Browser('chrome', view_mode=True)
    df = pd.read_csv('gb_url.csv')
    url = df.iloc[1].url

    service.d.get(url)


    def setup_tabs(_service: Browser, _tab_cnt: int):
        for _ in range(_tab_cnt):
            try:
                if _service.wait_selector(".bet_disable.on", wait_time=1):
                    return

                _service.d.execute_script(f"window.open('{df.iloc[1].bat_url}')")
                selector_all = _service.wait_selector_all(".powerball_row:nth-child(n + 4):nth-child(-n + 7) label")
                choice = random.choice(selector_all)
                _service.d.execute_script("arguments[0].click();", choice)
                _service.wait_selector('idCartBetMoney', by=By.ID).send_keys(MINIMUM_AMOUNT)
                if True:
                    continue
                _service.d.execute_script(f'javascript:goBet()')
                _service.d.switch_to.alert.accept()
            except Exception as _e:
                print(f"error cnt: {_}, error: {_e}")


    def bat_all(_service: Browser, _tab_cnt: int):
        for x in range(_tab_cnt + 1):
            choice = random.choice(_service.wait_selector_all(".powerball_row:nth-child(n + 4):nth-child(-n + 7)"))
            choice.click()


    try:

        service.login(login_sbuks)
        time.sleep(1)
        service.d.execute_script(f"location.href = '{df.iloc[1].bat_url}';")
        tab_cnt = 3
        setup_tabs(service, tab_cnt)
        # bat_all(service, tab_cnt)

        time.sleep(15)


    except Exception as e:
        print(f'{e}')
    finally:
        service.d.quit()
