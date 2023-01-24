import json
import time

import pandas as pd
import requests

_subnet = "test_v2_"
type = "POWER"

df = pd.read_csv("info.csv")
server_df = pd.read_csv("local_server.csv")
_id, cnt = df.iloc[0]
_host, _conn_url = server_df.iloc[0, 0], server_df.iloc[0, 1]


def next_steps(_type):
    for idx in range(cnt):
        _subnet_result = _subnet + "_" + str(idx)
        base_url = f"{_host}{_conn_url.replace('{conn}', _id).replace('{sub}', _subnet_result).replace('{type}', _type)}"
        response = requests.get(base_url, verify=False)
        print(base_url)
        # time.sleep(1)
        result = json.loads(response.text)
        print("batting :", result)
        _curr_amount = result['amount']
        _curr_choice = result['choice']

        selector_json = {
            "POWER": {
                "ODD": "#span_4",
                "EVEN": "#span_5"
            },
            "BASIC": {
                "ODD": "#span_0",
                "EVEN": "#span_1"
            }
        }
        print("result : ", result)
        _next_amount, _next_type, _next_choice = result['amount'], result['fiveType'], result['choice']
        print(_next_type, _next_choice, _next_amount)


if __name__ == '__main__':
    next_steps(type)
