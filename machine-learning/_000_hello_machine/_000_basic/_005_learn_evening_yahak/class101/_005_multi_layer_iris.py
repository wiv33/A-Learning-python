import pandas as pd
import tensorflow as tf

file_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris = pd.read_csv(file_path)

# iris[:].T[0:4].loc[:, []].index
encoding = pd.get_dummies(iris)
# print(encoding.columns)

독립 = encoding[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
종속 = encoding[['품종_setosa', '품종_versicolor', '품종_virginica']]

# print(독립 , end='\n')
# print(종속)

# 모델 구조 생성

X = tf.keras.layers.Input(shape=[4])

H = tf.keras.layers.Dense(8)(X)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation(activation='swish')(H)

H = tf.keras.layers.Dense(8)(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation(activation='swish')(H)

H = tf.keras.layers.Dense(8)(H)
H = tf.keras.layers.BatchNormalization()(H)
H = tf.keras.layers.Activation(activation='swish')(H)

Y = tf.keras.layers.Dense(3, activation='softmax')(H)
model = tf.keras.models.Model(X, Y)

model.compile(loss='categorical_crossentropy', metrics='accuracy')

# fit
model.fit(독립, 종속, epochs=1000, batch_size=150)

# 5/5 [==============================] - 0s 787us/step - loss: 0.0459 - accuracy: 0.9800
# Epoch 3333/3333
# 5/5 [==============================] - 0s 832us/step - loss: 0.0429 - accuracy: 0.9867
