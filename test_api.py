# Python3 샘플 코드 #


import requests
from kafka import KafkaProducer

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
params = {
    'serviceKey': 'WyceBdyEd%2FEwc2BUWA4bYkoyT79CmHVuoNjJVnDNWRymcrT7ZDKgBt4xRVObkKgYfhVJoT99NWSw7lx3GPFmmw%3D%3D',
    'LAWD_CD': '11100', 'DEAL_YMD': '2020012'}

response = requests.get(url, params=params)
print(response.content)

