import tensorflow as tf
import numpy as np

# 이해가지 않는 부분 추가 주식
# 분류기

x_data = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 0],
    [0, 0],
    [0, 1],
])


# (6, 3)
y_data = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 1]
])

"""신경망의 모듈을 만든다 """
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
W = tf.Variable(tf.random_uniform([2, 3], -1., 1.))

# 편향 값
# 처음은 0부터 시작하겠다는 의미
b = tf.Variable(tf.zeros([3]))

# 첫 번째 레이어
L = tf.add(tf.matmul(X, W), b)
# 활성함수
L = tf.nn.relu(L)

"""출력 값 얻기 softmax 함수"""
# 히든 레이어 1,2,3 를 지나 마지막 값을 model 이라고 칭한다.
model = tf.nn.softmax(L)

log = tf.log(model)
print(log)
cost = tf.reduce_mean(-tf.reduce_sum(Y * log, axis=1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(cost)

# 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(100):
        sess.run(train_op, feed_dict={X: x_data, Y: y_data})

        print("{} 번째 : {}".format(i, sess.run(cost, feed_dict={X: x_data, Y: y_data})))

    prediction = tf.argmax(model, 1)
    target = tf.argmax(Y, 1)

    print("예측: {}".format(sess.run(prediction, feed_dict={X: x_data})))
    print("실제: {}".format(sess.run(target, feed_dict={Y: y_data})))

    is_correct = tf.equal(prediction, target)

    cast = tf.cast(is_correct, dtype=tf.float32)

    accuracy = tf.reduce_mean(cast)

    print("정확도: {}".format(sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data})))

