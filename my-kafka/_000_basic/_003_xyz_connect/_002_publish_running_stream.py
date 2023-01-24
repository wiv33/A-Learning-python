import time

import pandas as pd
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium import webdriver

if __name__ == '__main__':

    async def batting(init_msg):
        print(init_msg)
        # time.sleep(40)
        reader = await requests.get(
            f"http://powerball.public.psawesome.xyz/v1/power-ball-choice/conn-id/{_id}/stream")

        data = await reader
        value = data.decode()
        print(f"val type is : {type(value)}")

        try:
            if b.switch_to.alert:
                print(b.switch_to.alert.text)
                time.sleep(2)
                b.switch_to.alert.accept()
                print("exists alert")
                try:
                    if b.switch_to.alert:
                        time.sleep(2)
                        b.switch_to.alert.accept()
                except Exception as __e:
                    if __e.__str__() != 'no such alert':
                        print(__e)
            else:
                print("not exists alert")
        except Exception as _e:
            if not _e.__str__().lower().__contains__('no such alert'):
                print(_e)

        print("check record val", value)

        selector_json = {
            "POWER_BALL": {
                "ODD": "#span_4",
                "EVEN": "#span_5"
            },
            "BASIC_BALL": {
                "ODD": "#span_0",
                "EVEN": "#span_1"
            }
        }

        _price, _type, _val = value['price'], value['choiceType'], value['choiceValue']

        b.execute_script("(function(){ window.print_y = 'Y' })();")
        b.execute_script(f'bat_money_change2({_price})')
        val_ = selector_json[_type][_val]
        b.find_element(By.CSS_SELECTOR, val_).click()
        b.execute_script(f'javascript:buy_ok()')

        print("=" * 33)
        print(
            f"\t\t다음 금액: {_price}\n"
            f"\t\t다음 타입: {_type}\n"
            f"\t\t다음 선택: {_val}")
        print("=" * 33)

        b.refresh()


    view_mode = False
    options = Options()
    if view_mode:
        options.add_argument('headless')

    options.add_argument("--window-size=2000,1000")
    options.add_argument('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/108.0.0.0 Whale/3.18.154.8 Safari/537.36')
    options.add_argument('lang=ko_KR')
    b = webdriver.Chrome(options=options)

    b.get("http://sm333.cc")
    account_df = pd.read_csv('account.csv')
    _id, _pw = account_df.iloc[0].id, account_df.iloc[0].pw
    b.find_element(By.CSS_SELECTOR, "#userid").send_keys(_id)
    b.find_element(By.CSS_SELECTOR, "#userpw").send_keys(_pw)
    b.save_screenshot('access_code.png')
    code = ""
    if view_mode:
        code = input("이미지에 보이는 보안 코드를 입력하세요: ")
        b.find_element(By.CSS_SELECTOR, ".codes").send_keys(code)
    else:
        b.find_element(By.CSS_SELECTOR, ".codes").send_keys(code)
        time.sleep(17)

    import asyncio

    try:

        b.switch_to.frame("live-iframe")
        sound = b.find_element(By.CSS_SELECTOR, "#btn_sound")
        b.execute_script("arguments[0].removeAttribute('on')", sound)
        b.switch_to.default_content()
        asyncio.run(batting("start batting"))

    except Exception as e:
        print("exit exception")
        print(e)
    finally:
        requests.delete(f"http://powerball.public.psawesome.xyz/v1/power-ball-choice/conn-id/{_id}")
        b.close()
        print("finally call delete request")

    requests.delete(f"http://powerball.public.psawesome.xyz/v1/power-ball-choice/conn-id/{_id}")
