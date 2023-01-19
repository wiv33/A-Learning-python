import sys
import time

import pandas as pd
from BrowserModule import Browser


def send_approval(account_info):
    print("sender : ", account_info)
    _id, _pw, _url = account_info

    d.get(_url)

    time.sleep(10)


if __name__ == '__main__':
    sender = "qwer3" if len(sys.argv) < 2 else sys.argv[0]
    account_df = pd.read_csv("account-beta.csv", index_col='_idx')
    sender_info = account_df.loc[sender]
    receiver_info = account_df.loc[account_df.index != sender]

    print(sender_info.to_list())

    b = Browser(view_mode=True)
    d = b.d

    send_approval(sender_info.to_list())

    d.quit()
