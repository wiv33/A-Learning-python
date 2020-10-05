import tensorflow as tf

"""간단한 분류 모델 구현
"""

x_data = [1,2,3]
y_data = [1,2,3]

# 하나의 텐서,
W = tf.Variable(tf.random_uniform([1], -0.1, 1.0))
b = tf.Variable(tf.random_uniform([1], -0.1, 1.0))

X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

hypothesis = W * X + b

# gradient = 기울기
# train.기울기_적절한_최적화
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op = optimizer.minimize(cost)

""" 
지도함수
입력값, 출력값 있는 상태에서
비용함수: cost
비용은 낮을 수록 좋은 것이므로
weight W 값을 낮추어
낮은 cost를 찾는 것.?
"""


