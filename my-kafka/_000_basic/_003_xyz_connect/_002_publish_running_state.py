import pandas as pd

from Crawling._001_extract_numbers._000_ace.BrowserModule import Browser
from _000_KafkaManager import KafkaManager

if __name__ == '__main__':

    manager = KafkaManager()

    service = Browser('chrome', True)
    url_df = pd.read_csv("gb_url.csv")
    service.d.get(url_df.iloc[1])
