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
Y = tf.keras.layers.Dense(3, activation='softmax')(X)
model = tf.keras.models.Model(X, Y)

model.compile(loss='categorical_crossentropy', metrics='accuracy')

# fit
model.fit(독립, 종속, epochs=333)

print(model.predict(독립[:5]))
print(종속[:5])

print(model.predict(독립[-5:]))
print(종속[-5:])

# weight
print("============================")
print(model.get_weights())

# [array([[-0.13242723,  0.17295605, -0.15411185],
#        [ 1.6041465 ,  0.20854329, -0.9012156 ],
#        [-1.0698128 , -0.21165888,  1.0220345 ],
#        [-0.7109205 ,  0.9873944 ,  0.85972345]], dtype=float32),
#        array([ 0.9745489 , -0.21749257, -0.6588568 ], dtype=float32)]
