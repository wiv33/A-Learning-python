import pandas as pd

df = pd.read_csv('data/precipitation_201910_202009.csv', encoding='utf-8')
columns = ['day', 'hour', 'precipitation']
df.columns = columns
print(df.head())
