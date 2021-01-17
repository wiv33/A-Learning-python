import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import utils, layers, models

print(tf.__version__)

# 신경망과 훈련 매개변수
EPOCHS = 200
BATCH_SIZE = 128
VERBEOSE = 1
NB_CLASSES = 10  # output의 demension
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2  # 검증

# MNIST 데이터셋 로드
# 검증

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
RESHAPED = 784

x_train = x_train.reshape(60000, RESHAPED)
x_test = x_test.reshape(10000, RESHAPED)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# scaling
x_train, x_test = x_train / 255., x_test / 255.

y_train = utils.to_categorical(y_train, NB_CLASSES)
y_test = utils.to_categorical(y_test, NB_CLASSES)

inputs = layers.Input(shape=RESHAPED)
H = layers.Dense(10, name='dense_layer_1')(inputs)
outputs = layers.Activation(activation='softmax')(H)

model = models.Model(inputs, outputs)

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy', 'mse'])

history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=128)

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])

plt.show()

evaluate = model.evaluate(x_test, y_test)

print('eval ', evaluate)
