import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, activations, optimizers, losses, utils
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

import numpy as np
import pandas as pd

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 정상적으로 대입했는지
assert x_train.shape[1:] == x_test.shape[1:]

y_train, y_test = utils.to_categorical(y_train), utils.to_categorical(y_test)

assert y_test.shape[1] == 10 and y_train.shape[1] == 10

# scaling x_train, x_test
x_train, x_test = x_train / 255., x_test / 255.

assert len(x_train[x_train > 1]) == 0

# extract evaluate data
extract_cnt = 10000
limit = len(x_train) - extract_cnt
x_train, y_train = x_train[extract_cnt:limit], y_train[extract_cnt:limit]
x_eval, y_eval = x_train[:extract_cnt], y_train[:extract_cnt]

# build model
<<<<<<< HEAD
inputs = layers.Input(shape=x_train.shape[1:])
=======
inputs = layers.Input(shape=(28, 28))
>>>>>>> d836ceaed17a253908325663a1bf0903fc40b5a2
H = layers.Flatten()(inputs)

H = layers.Dense(784)(H)
H = layers.Activation("swish")(H)

H = layers.Dense(256)(H)
H = layers.Activation("swish")(H)

H = layers.Dense(64)(H)

outputs = layers.Dense(10, activation="softmax")(H)

# compile model
model = models.Model(inputs, outputs)
model.compile(optimizer=optimizers.Adam(),
              loss=losses.categorical_crossentropy,
              metrics=['accuracy', 'mse'])

# fit model
history = model.fit(x_train,
                    y_train,
                    batch_size=64,
                    epochs=10,
                    validation_data=(x_test, y_test))

print(history.history['accuracy'])

