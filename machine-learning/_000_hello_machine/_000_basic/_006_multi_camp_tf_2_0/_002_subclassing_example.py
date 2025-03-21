# -*- coding: utf-8 -*-
"""SubClassing_example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VXVuYDb8oyWMxabO94JX1-sU8JmyJ_Aw
"""

import tensorflow as tf


class CustomModel(tf.keras.Model):
    def __init__(self):
        super(CustomModel, self).__init__(name='subclassing_exercise')
        self.flatten = tf.keras.layers.Flatten()
        self.fully_connected_1 = tf.keras.layers.Dense(256, activation='relu')
        self.fc2 = tf.keras.layers.Dense(128, activation='relu')
        self.dropout = tf.keras.layers.Dropout(rate=0.2)
        self.fc3 = tf.keras.layers.Dense(10, activation='softmax')

    def call(self, x):
        """ 생성자에 정의한 모델을 실행시키는 구간으로 input에 해당하는 x를 받아야 한다.
        :param x
        """
        x = self.flatten(x)
        x = self.fully_connected_1(x)
        x = self.fc2(x)
        x = self.dropout(x)
        x = self.fc3(x)
        return x


model = CustomModel()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
data = tf.keras.datasets.fashion_mnist.load_data()

(x_train, y_train), (x_test, y_test) = data

x_train, x_test = x_train / 255., x_test / 255.

model.fit(x_train, y_train, batch_size=10, epochs=5)
