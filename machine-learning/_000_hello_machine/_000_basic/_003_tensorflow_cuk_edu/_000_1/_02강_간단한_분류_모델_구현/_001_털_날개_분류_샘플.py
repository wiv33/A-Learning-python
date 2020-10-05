import tensorflow as tf
import numpy as np

# [털, 날개]
x_data = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 0],
    [0, 0],
    [0, 1]
])

# [기타, 포유류, 조류]
# 다음과 같은 형식을 one-hot 형식의 데이터라고 한다.
# 각 종류에 해당하는 인덱스(원하는 값이 1) 값만 1
# switch 방식
y_data = np.array([
    [1, 0, 0],  # 기타
    [0, 1, 0],  # 포유류
    [0, 0, 1],  # 조류
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 1]
])

# 데이터의 학습 정의 완료

# 특징 X와
X = tf.placeholder(tf.float32)
# 레이블 Y의 관계
Y = tf.placeholder(tf.float32)
# -> X와 Y는 placeholder

# 가중치와 편향 값
W = tf.Variable(tf.random_uniform([2, 3], -1., 1.))
# W: 가중치 -> [입력층, 출력층]

b = tf.Variable(tf.zeros([3]))
# b: 편향값


L = tf.add(tf.matmul(X, W), b)
L = tf.nn.relu(L)  # 활성함수를 이용한 것

# softmax 함수
# -> 배열 내의 결과값들을 전체 합이 1이 되도록 만들어줌
model = tf.nn.softmax(L)

# 예측값과 실제값 사이의 확률 분포 차이를 계산함
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(model), axis=1))

# 경사하강법
#
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

# 아래 minimize는 cost 값을 떨어지게 만든다.
train_op = optimizer.minimize(cost)

# 신경망 모델 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(1000):
        sess.run(train_op, feed_dict={X: x_data, Y: y_data})

        if (step + 1) % 10 == 0:
            print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))

    # result
    # 10 1.2383798
    # 20 1.2303792
    # 30 1.2226573
    # 40 1.2152051
    # 50 1.2080122
    # 60 1.2010698
    # 70 1.1943684
    # 80 1.1878991
    # 90 1.181653
    # 100 1.1756215

    prediction = tf.argmax(model, 1)

    target = tf.argmax(Y, 1) # 가장 큰 인덱스를 가져옴

    print("예측 값: {}".format(sess.run(prediction, feed_dict={X: x_data})))
    print("실제 값: {}".format(sess.run(target, feed_dict={Y: y_data})))

    # return equals: True, False
    is_correct = tf.equal(prediction, target)

    # cast: 0, 1로 변환
    cast = tf.cast(is_correct, tf.float32)

    accuracy = tf.reduce_mean(cast)
    print("정확도: %.2f" % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))

