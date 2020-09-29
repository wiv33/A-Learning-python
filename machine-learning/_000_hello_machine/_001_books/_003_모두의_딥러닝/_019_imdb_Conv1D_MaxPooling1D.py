import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from keras.callbacks import EarlyStopping
from keras.datasets import imdb
from keras.models import Model
from keras.preprocessing import sequence

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)

print(x_train.shape, y_train.shape)

# 데이터 전처리
x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)

print(x_train.shape, x_test.shape)

X = tf.keras.layers.Input(shape=100)
H = tf.keras.layers.Embedding(5000, 100)(X)
H = tf.keras.layers.Dropout(rate=0.5)(H)
# H = tf.keras.layers.Activation(activation='relu')(H)
H = tf.keras.layers.Activation(activation='swish')(H)
# H = tf.keras.layers.BatchNormalization()(H)

H = tf.keras.layers.Conv1D(64, 5, padding='valid', strides=1)(H)
H = tf.keras.layers.MaxPooling1D(pool_size=4)(H)
# H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.LSTM(55, activation='tanh')(H)

H = tf.keras.layers.Dense(1)(H)
Y = tf.keras.layers.Activation(activation='sigmoid')(H)

model = Model(X, Y)
model.summary()

# Model: "model"
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #
# =================================================================
# input_1 (InputLayer)         [(None, 5000)]            0
# _________________________________________________________________
# embedding (Embedding)        (None, 5000, 100)         500000
# _________________________________________________________________
# dropout (Dropout)            (None, 5000, 100)         0
# _________________________________________________________________
# conv1d (Conv1D)              (None, 4996, 64)          32064
# _________________________________________________________________
# max_pooling1d (MaxPooling1D) (None, 1249, 64)          0
# _________________________________________________________________
# lstm (LSTM)                  (None, 55)                26400
# _________________________________________________________________
# dense (Dense)                (None, 1)                 56
# _________________________________________________________________
# activation (Activation)      (None, 1)                 0
# =================================================================
# Total params: 558,520
# Trainable params: 558,520
# Non-trainable params: 0
# _________________________________________________________________
#

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

early_stopping_callback = EarlyStopping(monitor='val_loss', patience=2)
history = model.fit(x_train, y_train,
                    batch_size=100,
                    epochs=5,
                    callbacks=early_stopping_callback,
                    validation_data=(x_test, y_test))

print('\nTest Accuracy : %.4f' % (model.evaluate(x_test, y_test)[1]))

# 테스트셋의 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss']

# 그래프 표현
x_len = np.arange(len(y_loss))

plt.plot(x_len, y_vloss, marker='.', c='red', label="Test set loss")
plt.plot(x_len, y_loss, marker='.', c='yellow', label="Train set loss")

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

