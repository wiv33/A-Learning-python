import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

"""
    자유도가 높은 sub classing 구현
    필수 메서드
        * __init__
        * call
"""


class MyModel(tf.keras.Model):
    def __init__(self, hidden_dimension, hidden_dimension2, output_dimension):
        """
        사용방법:
            __init__: 모델에 사용될 층과 변수를 정의
            call: 모델의 연산을 진행

        :param hidden_dimension:
        :param hidden_dimension2:
        :param output_dimension:
        """
        super(MyModel, self).__init__(name='my model')
        self.dense_layer1 = layers.Dense(hidden_dimension, activation='swish')
        self.dense_layer2 = layers.Dense(hidden_dimension2, activation='swish')
        self.dense_layer3 = layers.Dense(output_dimension, activation='softmax')

    def call(self, inputs):
        x = self.dense_layer1(inputs)
        x = self.dense_layer2(x)
        return self.dense_layer3(x)

