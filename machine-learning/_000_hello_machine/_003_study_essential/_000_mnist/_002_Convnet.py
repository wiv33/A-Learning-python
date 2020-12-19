import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, activations, optimizers, losses, utils
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

import numpy as np
import pandas as pd

from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# one hot encoder
y_train = utils.to_categorical(y_train, 10)
y_test = utils.to_categorical(y_test, 10)

# scale 0 or 1
x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# divide `train data` and `eval data`
x_train, x_eval = x_train[:50000, ], x_train[50000:, ]
y_train, y_eval = y_train[:50000, ], y_train[50000:, ]

print(f'x_train shape: {x_train.shape}')

# build model
X = layers.Input(shape=(28, 28, 1))

H = layers.Conv2D(32, kernel_size=(3, 3))(X)
# H = layers.BatchNormalization()(H)
H = layers.Activation('swish')(H)
H = layers.MaxPooling2D(pool_size=(2, 2))(H)

H = layers.Dropout(.3)(H)
H = layers.Conv2D(64, kernel_size=(3, 3))(H)
# H = layers.BatchNormalization()(H)
H = layers.Activation('swish')(H)
H = layers.MaxPooling2D(pool_size=(2, 2))(H)

H = layers.Flatten()(H)
H = layers.Dropout(.3)(H)

Y = layers.Dense(10)(H)
Y = layers.Activation('softmax')(Y)

model = models.Model(X, Y)

print(model.summary())

# train model

model.compile(loss=losses.categorical_crossentropy,
              optimizer='adam',
              metrics='accuracy')

model.fit(x_train, y_train, batch_size=32,
          epochs=5,
          validation_data=(x_test, y_test),
          validation_split=.2)

# evaluate model
score = model.evaluate(x_eval, y_eval, verbose=False)

visit = lambda name, sc: print('{}: {:.4f}'.format(name, sc))
visit('loss', score[0])
visit('accuracy', score[1])
