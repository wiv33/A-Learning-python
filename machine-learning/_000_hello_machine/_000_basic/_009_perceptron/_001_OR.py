import tensorflow as tf


def OR():
    F = .0
    T = 1.
    bias = 1.
    X = [
        [F, F, bias],
        [F, T, bias],
        [T, F, bias],
        [T, T, bias],
    ]
    Y = [
        [F],
        [T],
        [T],
        [T],
    ]
    return X, Y


x, y = OR()

print(x, y)

W = tf.Variable(tf.random.normal([3, 1]))
print(W)


def step(x):
    return float(tf.greater(x, 0))


print(step(x))

# def loss_function(X, W, Y):
f = tf.matmul(x, W)
output = step(f)
error = tf.subtract(y, output)
mse = tf.reduce_mean(tf.square(error))

delta = tf.matmul(x, error, transpose_a=True)
train = tf.asin(W, tf.add(W, delta))

