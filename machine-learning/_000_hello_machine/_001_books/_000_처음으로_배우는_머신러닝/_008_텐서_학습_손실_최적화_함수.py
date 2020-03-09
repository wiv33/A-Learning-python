import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

boston = datasets.load_boston()
boston_slice = [x[5] for x in boston.data]

data_x = np.array(boston_slice).reshape(-1, 1)  # == np.array(boston_slice).reshape(506, 1)
data_y = boston.target.reshape(-1, 1)

n_sample = data_x.shape[0]

X = tf.placeholder(tf.float32, shape=(n_sample, 1), name="X")
y = tf.placeholder(tf.float32, shape=(n_sample, 1), name='y')

W = tf.Variable(tf.zeros((1, 1)), name="weights")
b = tf.Variable(tf.zeros((1,1)), name="bias")

"""_007_ 이후 추가 로직

"""
y_pred = tf.matmul(X, W) + b # 모델

loss = tf.reduce_mean(tf.square(y_pred - y)) # 손실함수

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001) # 최적화 클래스
train_op = optimizer.minimize(loss) # 최적화 함수. 손실함수의 최솟값을 찾는다.
summary_op = tf.summary.scalar('loss', loss) # 시각화를 위한 서머리 함수. 손실함수의 변화를 기록한다.

