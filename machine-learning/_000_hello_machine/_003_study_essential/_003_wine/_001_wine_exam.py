import pandas as pd
import tensorflow as tf
from tensorflow.keras import models, layers, losses
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

assert "2.3.1" == tf.__version__

seed = 3
np.random.seed(seed)
# tf.random.set_seed(seed)


df = pd.read_csv("https://raw.githubusercontent.com/wiv33/A-Learning-python/master/machine-learning"
                 "/_000_hello_machine/_003_study_essential/_003_wine/data/wine.csv")

x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1])

inputs = layers.Input(shape=(x_train.shape[1]))

h = layers.Dense(32)(inputs)
h = layers.BatchNormalization()(h)
h = layers.Activation('swish')(h)

h = layers.Dropout(.3)(h)
h = layers.Dense(12)(h)
h = layers.BatchNormalization()(h)
h = layers.Activation('swish')(h)

h = layers.Dropout(.5)(h)
h = layers.Dense(8)(h)
h = layers.BatchNormalization()(h)
h = layers.Activation('swish')(h)

h = layers.Dense(1)(h)
output = layers.Activation('sigmoid')(h)

model = models.Model(inputs, output)

model.compile(loss=losses.mean_squared_error,
              optimizer='adam',
              metrics='accuracy')

history = model.fit(x_train, y_train,
                    batch_size=32,
                    epochs=100,
                    validation_data=(x_test, y_test),
                    validation_split=.3,
                    verbose=0)


plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.show()

print(model.evaluate(x_test, y_test)[1])




