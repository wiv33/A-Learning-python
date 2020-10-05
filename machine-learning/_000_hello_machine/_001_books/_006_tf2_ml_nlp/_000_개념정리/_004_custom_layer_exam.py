import tensorflow as tf
from tensorflow.keras import layers


class CustomLayer(layers.Layer):

    def __init__(self, hidden_dimension, hidden_dimension2, output_dimension):
        self.hidden_dimension2 = hidden_dimension2
        self.output_dimension = output_dimension
        self.hidden_dimension = hidden_dimension
        super(CustomLayer, self).__init__()

    def build(self, input_shape):
        self.dense_layer1 = layers.Dense(self.hidden_dimension, activation='relu')
        self.dense_layer2 = layers.Dense(self.hidden_dimension2, activation='relu')
        self.dense_layer3 = layers.Dense(self.output_dimension, activation='softmax')

    def call(self, inputs):
        x = self.dense_layer1(inputs)
        x = self.dense_layer2(x)
        return self.dense_layer3(x)


model = tf.keras.Sequential()
model.add(CustomLayer(64, 64, 10))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

