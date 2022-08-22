import pandas as pd
import lxml
import requests
res = requests.get('https://api.odcloud.kr/api/15093209/v1/uddi:d4cca88c-a7d1-4be7-9b32-c94466150f57?page=1&perPage=1000&returnType=XML&serviceKey=WyceBdyEd%2FEwc2BUWA4bYkoyT79CmHVuoNjJVnDNWRymcrT7ZDKgBt4xRVObkKgYfhVJoT99NWSw7lx3GPFmmw%3D%3D')
print(res.text)
xml = f'''<?xml version='1.0' encoding='utf-8'?>
{res.text}'''
df = pd.read_xml(xml)

df.head()