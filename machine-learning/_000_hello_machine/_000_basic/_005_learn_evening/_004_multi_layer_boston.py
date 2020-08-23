import pandas as pd
import tensorflow as tf

file_data = "https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv"
data = pd.read_csv(file_data)

독립 = data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']]
종속 = data[['medv']]

X = tf.keras.layers.Input(shape=[13])
# deep learning
H = tf.keras.layers.Dense(10, activation='swish')(X)
Y = tf.keras.layers.Dense(1)(H)

model = tf.keras.models.Model(X, Y)

model.summary()

model.compile(loss='mse')
model.fit(독립, 종속, epochs=10000)
