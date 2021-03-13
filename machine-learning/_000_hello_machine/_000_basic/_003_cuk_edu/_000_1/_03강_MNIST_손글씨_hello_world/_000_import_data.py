import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 28 * 28
X = tf.placeholder(tf.float32, [None, 784])
Y = tf.palceholder(tf.float32, [None, 10])

# 첫 번째 레이어
# 256은 뉴런의 개수
W1 = tf.Variable(tf.random_normal([784, 256]))
L1 = tf.nn.relu(tf.matmul(X, W1))  # relu => 활성화 함수, 행렬의 곱

# 두 번째 레이어
W2 = tf.Variable(tf.random_normal([256, 256]))
L2 = tf.nn.relu(tf.matmul(L1, W2)) # 첫 번째 레이어가 입력 값

# 세 번째 레이어 -> 출력 레이어
W3 = tf.Variable(tf.random_normal([256, 256]))
model = tf.matmul(L2, W3)


cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)



