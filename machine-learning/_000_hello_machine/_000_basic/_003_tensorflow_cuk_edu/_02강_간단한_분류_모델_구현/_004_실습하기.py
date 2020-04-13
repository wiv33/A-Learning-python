import tensorflow as tf

x_data = [1,2,3] # 입력
y_data = [1,2,3] # 출력

# -1에서부터 1까지의 균등 분포를 확인
# TODO uniform 과 normal의 차이를 알아야한다.
W = tf.Variable(tf.random_uniform([1], -1., 1.))
b = tf.Variable(tf.random_uniform([1], -1., 1.))

# 입력값을 받는
X = tf.placeholder(tf.float32, name="X")
# X1 = tf.placeholder(tf.float32)
# 이름 없음 결과
# print(X1)
# Tensor("Placeholder:0", dtype=float32)
Y = tf.placeholder(tf.float32, name="Y")

# 2차 함수
# W 가중치
# b 편향
# 선형 회귀 분석을 할 때 기본이 되는 수식
# 뉴럴 네트워크 기본
hypothesis = X * W + b

print(hypothesis)

# 손실함수
# cost = error
# 비용이 점점 절감되는 방향으로 가야한다.
# 어떤 의미?
# hypothesis = 결과 값
# y는 우리가 알고 있는 값
# 예측을 했을 때 예측 값에서 실제 값을 뺀 것
# 에러 값이 높으니까 점점 낮아질 값으로 weight 를 변경한다.
# 가장 낮아지는 weight 값을 찾는 것
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1) # 방향성을 제시하기 위해 해당 함수를 사용
train_op = optimizer.minimize(cost)

# 모델링 끝

# 경사하강법을 사용하였다.
# 계속 작아지는 값으로 이동하는 것

with tf.Session() as sess:
    # 텐서 초기화
    sess.run(tf.global_variables_initializer())

    for step in range(100):
        # print(train_op)
        # print(cost)
        _, cost_val = sess.run([train_op, cost], feed_dict={X: x_data, Y: y_data})
        print("{} 번째 : {}, {}, {}".format(step, cost_val, sess.run(W), sess.run(b)))

    print("\n === Test ===")
    print("X:5, Y:", sess.run(hypothesis, feed_dict={X: 5}))
    print("X:2.5, Y:", sess.run(hypothesis, feed_dict={X: 2.5}))

