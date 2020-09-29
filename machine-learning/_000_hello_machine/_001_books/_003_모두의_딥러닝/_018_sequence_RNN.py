import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import reuters
from keras.layers import Embedding, LSTM, Dense, BatchNormalization, Activation
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.utils import np_utils

(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=1000)

print(x_train.shape)
print(y_train)
category = np.max(y_train) + 1
print(category)
print(len(x_train), '학습용 뉴스 기사')
print(len(x_test), '테스트용 뉴스 기사')
print(x_train[0])

# x_train.shape >>> (8982,)
# colum의 길이를 sequence를 통해 맞춘다.
# data 전처리
x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)

# print(x_test.shape, ' x shape')

# y인 카테고리에 원-핫 인코딩
# print(y_train)
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# print(y_train.shape, ' y shape')
# print(y_train[0])

model = Sequential()
model.add(Embedding(1000, 100))
model.add(BatchNormalization())
model.add(Activation(activation='tanh'))
model.add(LSTM(100))
model.add(Dense(46, activation='softmax'))

# inputs = Input(shape=46)

# x = Embedding(1000, 100)(inputs)
# x = BatchNormalization()(x)
# x = Activation(activation='tanh')(x)
#
# x = LSTM(100)(x)
# x = BatchNormalization()(x)
# x = Activation(activation='softmax')(x)
#
# model = Model(inputs, x)

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=100, epochs=20,
                    validation_data=(x_test, y_test))

model.summary()

# 테스트 정확도 출력
print("Test Accuracy {}".format(model.evaluate(x_test, y_test)[1]))

# 테스트셋 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss']

# 그래프
x_len = np.arrange(len(y_loss))

plt.plot(x_len, y_vloss, marker='.', c='red', label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c='blue', label='Trainset_loss')

# 그래프에 그리드를 추가하고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
