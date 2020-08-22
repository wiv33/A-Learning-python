import pandas as pd
import tensorflow as tf

file_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
data = pd.read_csv(file_path)

독립 = data[['온도']]
종속 = data[['판매량']]

print(data.head())

X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)

model = tf.keras.models.Model(X, Y)

model.compile(loss='mse')
model.fit(독립, 종속, epochs=10000, verbose=0)

result = model.predict([[15]])

print(result)
