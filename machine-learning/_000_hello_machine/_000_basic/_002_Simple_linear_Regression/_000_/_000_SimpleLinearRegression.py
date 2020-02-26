import numpy as np
import tensorflow as tf

x_data = range(1, 6)
y_data = range(1, 6)

W = tf.Variable(2.9)
b = tf.Variable(0.5)

# hypothesis = W * x + b
hypothesis = W * x_data + b

