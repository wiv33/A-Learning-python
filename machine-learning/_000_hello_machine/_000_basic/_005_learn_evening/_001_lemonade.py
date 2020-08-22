import pandas as pd
import tensorflow as tf

file_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
data = pd.read_csv(file_path)

독립 = data[['온도']]
종속 = data[['판매량']]
print(독립.shape, 종속.shape)

# 모델의 구조 만들기

tf.keras
