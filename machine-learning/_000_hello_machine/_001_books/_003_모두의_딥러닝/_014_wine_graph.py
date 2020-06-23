from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

import pandas as pd
import numpy as np

import os
import matplotlib.pyplot as plt
import tensorflow as tf

# seed 값 설정
np.random.seed(3)
tf.random.set_seed(3)
"""
wine.csv data - 농도 표기
0: 주석산                      12: class(1: 레드와인, 0: 화이트와인)
1: 아세트산
2: 구연산
3: 잔류 당분
4: 염화나트륨
5: 유리 아황산
6: 총 아황산
7: 밀도       
8: pH
9: 황산칼륨
10: 알코올 도수
11: 와인의 맛 등급 (0 ~ 10)
"""
df_pre = pd.read_csv('dataset/wine.csv', header=None)
df = df_pre.sample(frac=0.15)

dataset = df.values
X = dataset[:, 0: 12]
Y = dataset[:, 12]

# 모델의 설정
model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # 마지막은 sigmoid

# 모델 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 과적합 학습 자동 중단 설정
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=100)

# 모델 저장 폴더 설정
MODEL_DIR = './wine/model/'
if not os.path.exists(MODEL_DIR):
    """존재하지 않을 때 dirs 생성"""
    os.makedirs(MODEL_DIR)

# 모델 저장 조건 설정
model_path = './wine/model/{epoch:02d}-{val_loss:.4f}.hdf5'
check_pointer = ModelCheckpoint(filepath=model_path, monitor='val_loss', verbose=1, save_best_only=True)

# 모델 실행 및 저장
history = model.fit(X, Y, validation_split=0.2, epochs=2000, batch_size=500, verbose=1,
                    callbacks=[early_stopping_callback, check_pointer])

# y_vloss 에 테스트 셋으로 실험 결과의 오차 값을 저장
y_vloss = history.history['val_loss']

# y_acc 에 학습셋으로 측정한 정확도의 값을 저장
y_acc = history.history['val_accuracy']

# x 값을 지정하고 정확도를 파란색으로, 오차를 빨간색으로 표시
x_len = np.arange(len(y_acc))
plt.plot(x_len, y_vloss, 'o', c='red', markersize=3)
plt.plot(x_len, y_acc, 'o', c='blue', markersize=3)

plt.show()
