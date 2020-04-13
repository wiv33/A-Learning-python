import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

# 첫 번째 레이어
W1 = tf.Variable(tf.random_normal([784, 256], stddev=0.01))
L1 = tf.nn.relu(tf.matmul(X, W1))  # relu => 활성화 함수, 행렬의 곱
L1 = tf.nn.dropout(L1, keep_prob)

# 두 번째 레이어
W2 = tf.Variable(tf.random_normal([256, 256], stddev=0.01))
L2 = tf.nn.relu(tf.matmul(L1, W2)) # 첫 번째 레이어가 입력 값
L2 = tf.nn.dropout(L2, keep_prob)

# 세 번째 레이어 -> 출력 레이어
W3 = tf.Variable(tf.random_normal([256, 10], stddev=0.01))
model = tf.matmul(L2, W3)


cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)


# 학습을 위한 초기화
# ------------------------------------------------------------------------------------------
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size)

# 학습 부분
# ------------------------------------------------------------------------------------------
for epoch in range(15):
    total_cost = 0

    # batch를 이용하여 cost를 계산하고 전체 cost를 구하는 것
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)

        # 학습 시 drop_out 은 80%
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs,
                                                             Y: batch_ys,
                                                             keep_prob: 0.8})
        total_cost += cost_val

    print("Epoch: ", '%04d' % (epoch + 1), 'Avg. cost = ', '{:.3f}'.format(total_cost / total_batch))

print("최적화 완료")
# ------------------------------------------------------------------------------------------

# 실행(예측, 확인, 테스트 값)
# ------------------------------------------------------------------------------------------
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1)) # 정확도를 위해 계산
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32)) # 정확도를 계산

print('정확도: ', sess.run(accuracy, feed_dict={X: mnist.test.images,
                                             Y: mnist.test.labels,
                                             keep_prob: 1}))

labels = sess.run(model, feed_dict={X: mnist.test.images,
                                             Y: mnist.test.labels,
                                             keep_prob: 1})

# 결과 값 그리기
fig = plt.figure()
for i in range(10):
    subplot = fig.add_subplot(2, 5, i + 1)
    subplot.set_xticks([])
    subplot.set_yticks([])
    subplot.set_title('%d' % np.argmax(labels[i]))
    subplot.imshow(mnist.test.images[i].reshape((28, 28)), cmap=plt.cm.gray_r)

plt.show()
# ------------------------------------------------------------------------------------------