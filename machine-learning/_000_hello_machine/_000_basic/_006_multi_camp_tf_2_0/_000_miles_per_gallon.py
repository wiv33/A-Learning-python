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

train_labels = train_dataset.pop("MPG")
test_labels = test_dataset.pop("MPG")


# 표준화 작업
def normalization(x):
    # 평균 값을 빼고, 표준 편차로 나누어준다.
    normed_data = ((x - train_stats['mean']) / train_stats['std'])
    return normed_data


train_dataset = normalization(train_dataset)
test_dataset = normalization(test_dataset)

print(train_dataset.describe())

# hidden layer : 2개[65, 32], activation: relu
model = models.Sequential()
model.add(layers.Dense(units=64, activation='relu', input_shape=(len(train_dataset.keys))))
model.add(layers.Dense(units=32, activation='relu'))
model.add(layers.Dense(units=1))

print(model.summary())
#
# rmspropablity
# gradient decent 보다 발전된 버전 / 하는 행위는 비슷하다고 함
# 기존 mean square error는 제곱
# mae 절대값을 취해서 실제 정답값과 차이를 직관적으로 보기 위한 설정
model.compile(loss='mse', optimizer='rmsprop', metrics='mae')

# 학습 진행

# batch size: 16, epochs : 100, validation data set percent : 20%

history = model.fit(
    x=train_dataset,
    y=train_labels,
    batch_size=16,
    epochs=100,
    validation_split=0.2
)

# 학습과정 시각화 및 성능 테스트
hist = pd.DataFrame(history.history)
print(hist)

loss = history.history['loss']
val_loss = history.history['val_loss']

mae = history.history['mae']
val_mae = history.history['val_mae']

# 차트의 x축을 위한 epochs
epochs = range(1, (len(loss) + 1))

plt.plot(epochs, loss, label='Training loss')
plt.plot(epochs, val_loss, label="Validation loss")
plt.title('Traning and validation loss')
plt.ylim([0, 20])
plt.legend()
plt.show()

plt.plot(epochs, mae, label='Training mae')
plt.plot(epochs, val_mae, label="Validation mae")
plt.title('Traning and validation mae')
plt.xlim([1, 100])
plt.ylim([0, 5])
plt.legend()
plt.show()


# 테스트 데이터 셋을 통한 성능 측정
test_loss, test_mae = model.evaluate(x=test_dataset, y=test_labels)

# 1.9 정도의 오차를 확인할 수 있었다.
# 사용자가 실제 모델의 성능을 체크하면 된다.

# 정답 데이터와 모델이 예측한 데이터의 상관관계 예측하기
# .flatten() : batch size로 축이 하나 더 생겨서 나온다.
test_predictions = model.predict(test_dataset).flatten()

plt.scatter(test_labels, test_predictions)
plt.xlabel("True values [MPG]")
plt.ylabel("Predictions [MPG]")
plt.axis('equal')
plt.axis('square')
plt.xlim([0, 50])
plt.ylim([0, 50])
_ = plt.plot([-100, 100], [-100, 100])
_.show()
plt.show()
