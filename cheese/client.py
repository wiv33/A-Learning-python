import json
import re
import time
import schedule

import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from concurrent.futures import ThreadPoolExecutor


def wait_selector(d, selector, wait_time=5, by=By.CSS_SELECTOR):
    return WebDriverWait(d, wait_time).until((
        ec.presence_of_element_located(
            (by, selector)
        )
    ))


def wait_selector_all(d, selector, wait_time=5, by=By.CSS_SELECTOR):
    return WebDriverWait(d, wait_time).until((
        ec.presence_of_all_elements_located(
            (by, selector)
        )
    ))


_subnet = "ps_v1_"
type_result = {
    "POWER_OE": "[EOS]",
    "POWER_UO": "[EOS]",
    "BASIC_OE": "[일반불]",
    "BASIC_UO": "[일반불]"
}
type_idx = {
    "POWER_OE": 0,
    "BASIC_OE": 0,
    "POWER_UO": 0,
    "BASIC_UO": 0
}

MIN_AMOUNT = 100
MAX_AMOUNT = 1_000_000

# server_df = pd.read_csv("server.csv")
_id, cnt = "sun18", 1


# _host, _conn_url = server_df.iloc[0]


def steps(_type):
    next_steps(_type)
    schedule.every(3).minutes.do(next_steps, _type)


if __name__ == '__main__':
    def next_steps(_type):
        waiting()

        for idx in range(cnt):
            response = get_next_response(_type)
            if not response:
                continue
            result = response
            print("batting info", result)
            _curr_amount = result['amount']
            _curr_choice = result['choice']

            selector_json = {
                "POWER_OE": {
                    "ODD": "#span_4",
                    "EVEN": "#span_5"
                },
                "BASIC_OE": {
                    "ODD": "#span_0",
                    "EVEN": "#span_1"
                },
                "POWER_UO": {
                    "UNDER": "#span_6",
                    "OVER": "#span_7",
                },
                "BASIC_UO": {
                    "UNDER": "#span_2",
                    "OVER": "#span_3",
                }
            }
            # print("result : ", result)
            _next_amount, _next_type, _next_choice = result['amount'], result['fiveType'], result['choice']
            time.sleep(1)
            b.execute_script("(function(){ window.print_y = 'Y'})();")
            b.execute_script(f'bat_money_change2({_next_amount})')
            bat_btn = b.find_element(By.CSS_SELECTOR, selector_json[_next_type][_next_choice])
            b.execute_script("arguments[0].click();", bat_btn)
            b.execute_script(f'javascript:buy_ok()')
            print("=" * 33)
            print(
                f"\t\t배팅 금액: {_next_amount}\n"
                f"\t\t배팅 타입: {_type}\n"
                f"\t\t배팅 선택: {_next_choice}")
            print("=" * 33)
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
        # b.refresh()
        print(wait_selector(b, "#top-info > div > div.float-left > span:nth-child(2)").text)
        time.sleep(1)


    def waiting():
        _cnt = 0
        while True:
            try:
                print(f"check available time ... {_cnt}")
                starting_time = wait_selector(b, "#limit_time", wait_time=30)
                sub_text = re.sub('\\D', "", starting_time.text)
                if sub_text and int(sub_text) > 50:
                    break
                time.sleep(10)
                _cnt += 10
            except Exception as _e:
                _cnt += 10
                print(f"starting is not available retry seconds {_cnt}...", _e.__str__())
        print("start next batting ...")


    def get_next_response(_type):
        # _subnet_result = _subnet + "_" + str(idx)
        # base_url = f"{_host}{_conn_url.replace('{conn}', _id).replace('{sub}', _subnet_result).replace('{type}', _type)}"
        # response = requests.get(base_url, verify=False)
        # print(base_url)
        type_map = {
            "POWER_OE": ["ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN"],
            "POWER_UO": ["UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER",
                         "OVER"],
            "BASIC_OE": ["ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN", "ODD", "EVEN"],
            "BASIC_UO": ["UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER", "OVER", "UNDER",
                         "OVER"],
        }
        convert_type_map = {
            "POWER_OE": ["홀", "짝"],
            "POWER_UO": ["언더", "오버"],
            "BASIC_OE": ["홀", "짝"],
            "BASIC_UO": ["언더", "오버"]
        }

        next_amount = MIN_AMOUNT
        print("check point 1")

        time.sleep(1)
        # while len(tr_all) == 0:
        #     try:
        print("try retrieve bat list ...")

        if len(wait_selector_all(b, "#batlist tr", wait_time=30)) < 4:
            result = {
                "fiveType": _type,
                "choice": type_map[_type][type_idx[_type]],
                "amount": MIN_AMOUNT
            }
            type_idx[_type] += 1
            return result

        bat_cnt = 1
        while True:
            _tr_ele_txt = None
            while _tr_ele_txt is None:
                try:
                    _tr_ele_txt = wait_selector(b,
                                                f"#batlist tr:nth-child({bat_cnt}) td:nth-child({bat_cnt})").find_element(
                        By.XPATH, '..').text
                    b.refresh()
                    time.sleep(1)
                except Exception as __e:
                    time.sleep(1)
                    b.refresh()
                    if bat_cnt > 10:
                        print(f"배팅 기록이 없어서 초기화됩니다. : {_type}, {type_map[_type][type_idx[_type]]}")
                        result = {
                            "fiveType": _type,
                            "choice": type_map[_type][type_idx[_type]],
                            "amount": MIN_AMOUNT
                        }
                        type_idx[_type] += 1
                        return result

                    print("retry extract text not attached ... ", bat_cnt)

            # print(_tr_ele_txt)
            if re.search("결과대기", _tr_ele_txt):
                _wait_texts = _tr_ele_txt.split(" ")
                if _wait_texts[0] == type_result[_type] and _wait_texts[1].split("\n")[0] in convert_type_map[_type]:
                    print(f"결과 대기중 : {_wait_texts[0]}, {_wait_texts[1]}")
                    return None
                bat_cnt += 1
                continue

            _type_info, _choice_info, _ratio, _result_txt, _amount, _result_amount, _date = _tr_ele_txt.split(" ")
            _choice_info = _choice_info.split("\n")[0]
            # print(
            #     f"type match : {_type_info} == {type_result[_type]}, "
            #     f"choice in : {_choice_info} in {convert_type_map[_type]}"
            # )
            if _type_info == type_result[_type] and _choice_info in convert_type_map[_type]:
                print(f"type is : {_type_info}, result text: {_result_txt}")

                if _result_txt.__contains__("미적중"):
                    clean_amount = re.sub("\\D", "", _amount)
                    print(f"last amount: {clean_amount}")
                    next_amount = int((int(clean_amount) * 2.2) // 10 * 10)
                else:
                    next_amount = MIN_AMOUNT

                print(f"next amount: {next_amount}")
                break

            bat_cnt += 1

        result = {
            "fiveType": _type,
            "choice": type_map[_type][type_idx[_type]],
            "amount": next_amount
        }
        type_idx[_type] += 1
        if type_idx[_type] >= len(type_map[_type]):
            type_idx[_type] = 0
        return result


    print(_id, cnt)

    view_mode = True
    options = Options()
    if not view_mode:
        options.add_argument('headless')

    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    options.add_argument('lang=ko_KR')
    b = webdriver.Chrome(options=options)
    cookie_dict = {}
    account_df = pd.read_csv('account.csv')
    _id, _pw, _url = account_df.iloc[0].id, account_df.iloc[0].pw, account_df.iloc[0].url
    b.get(_url)

    b.find_element(By.CSS_SELECTOR, "#userid").send_keys(_id)
    b.find_element(By.CSS_SELECTOR, "#userpw").send_keys(_pw)
    code = ""

    if not view_mode:
        b.save_screenshot('access_code.png')
        code = input("이미지에 보이는 보안 코드를 입력하세요: ")
        b.find_element(By.CSS_SELECTOR, ".codes").send_keys(code)
    else:
        b.find_element(By.CSS_SELECTOR, ".codes").send_keys(code)

    # b.implicitly_wait(15)
    time.sleep(12)

    try:
        b.switch_to.frame("live-iframe")
        sound = b.find_element(By.CSS_SELECTOR, "#btn_sound")
        b.execute_script("arguments[0].removeAttribute('on')", sound)
        b.switch_to.default_content()

        _cookies = b.get_cookies()

        for c in _cookies:
            cookie_dict[c['name']] = c['value']
            options.add_argument(f"{cookie_dict[c['name']]}={c['value']}")

        print(b.capabilities)
        print("init bat info", _id, _subnet)

        # steps("POWER_OE")
        # steps("POWER_UO")
        # steps("BASIC_OE")
        # steps("BASIC_UO")
        steps("POWER_OE")
        steps("POWER_UO")
        steps("BASIC_OE")
        steps("BASIC_UO")

        while True:
            schedule.run_pending()
            # with ThreadPoolExecutor() as executor:
            # res = executor.map(next_steps, ["POWER_OE", "POWER_UO"], chunksize=2)
            # res2 = executor.map(next_steps, ["BASIC_OE", "BASIC_UO"], chunksize=2)
            b.refresh()
            time.sleep(266)
    except Exception as e:
        print(e)
        print("exit exception")
    finally:
        b.close()
