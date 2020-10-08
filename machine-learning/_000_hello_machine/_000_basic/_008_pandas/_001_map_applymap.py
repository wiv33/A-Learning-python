import pandas as pd

date_list = [
    {'date': '2020-02-17'},
    {'date': '2020-07-27'},
    {'date': '2020-01-31'}
]
df = pd.DataFrame(date_list, columns=['date'])

print(df.head())


def extract_year(date):
    return date.split('-')[0]


df['year'] = df['date'].apply(extract_year)
print(df.head())

job_list = [
    {'age': 20, 'job': 'student'},
    {'age': 30, 'job': 'developer'},
    {'age': 20, 'job': 'teacher'},
]

df_job = pd.DataFrame(job_list)
print(df_job.head())

df_job.job = df_job.job.map({'student': 1, 'developer': 2, 'teacher': 3})
print(df_job.head())

# 모든 원소에 적용하고 싶을 때 applymap을 사용하면 된다.
import numpy as np

ran = np.random.randn(3, 3)
print(ran)

df_nums = pd.DataFrame(data=ran, columns=['x', 'y', 'z'])
print(df_nums.head())

df_square = df_nums.applymap(lambda x: x ** 2).applymap(np.around)
print(df_square.head())

