import tensorflow as tf
from tensorflow.keras import layers, models
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

auto_mpg_dataset_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
dataset_path = tf.keras.utils.get_file("./content/auto-mpg.data", auto_mpg_dataset_url)

print(dataset_path)

# 자동차 연비 데이터 셋의 컬럼
column_names = ['MPG', 'cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', "Origin"]

raw_dataset = pd.read_csv(dataset_path, names=column_names,
                          na_values='?', comment='\t',
                          sep=' ', skipinitialspace=True)

dataset = raw_dataset.copy()

# 데이터 전처리

# 1. na 확인
print(dataset.isna().sum())

# 2. Nan 제거
dataset = dataset.dropna()

print(len(dataset))

print(dataset.isna().sum())

# 데이터 셋 중 20% 선택하여 test 데이터 셋으로 분할
# frac: 어떤 비율로 데이터를 쪼갤 것인지
# random_state: 여러 번 실행해도 동일한 값이 나오도록 0으로 설정
train_dataset = dataset.sample(frac=0.8, random_state=0)

# 0.8 제외한 나머지로 데이터 셋을 설정
test_dataset = dataset.drop(train_dataset)

print(len(train_dataset))
print(len(test_dataset))

#
train_stats = train_dataset.describe()

# 정답 데이터 컬럼 제거
train_stats.pop("MPG")

print(train_stats)

# row, column 변경
train_stats = train_stats.transpose()

train_dataset = train_dataset.pop("MPG")
test_labels = test_dataset.pop("MPG")


# 표준화 작업
def normalization(x):
    # 평균 값을 빼고, 표준 편차로 나누어준다.
    normed_data = ((x - train_stats['mean']) / train_stats['std'])
    return normed_data


train_dataset = normalization(train_dataset)
test_dataset = normalization(test_dataset)

print(train_dataset.describe())