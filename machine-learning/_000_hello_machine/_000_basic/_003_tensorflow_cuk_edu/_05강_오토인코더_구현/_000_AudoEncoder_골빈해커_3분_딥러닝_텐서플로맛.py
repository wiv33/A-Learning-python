"""대표적인 비지도 학습법 AutoEncoder
- 지도 학습 (supervised learning)
    * 프로그램에게 원하는 결과를 알려주고 학습하게 하는 방법
    * X와 Y가 둘 다 있는 상태에서 학습

- 비지도 학습 (unsupervised learning)
    * 입력값으로부터 데이터의 특징을 찾아내는 학습 방법
    * X만 있는 상태에서 학습
    * 오토인코더(AutoEncoder): 비지도 학습 중 가장 널리 쓰이는 신경망


오토인코더 개념

- 입력값과 출력값을 같게 하는 신경망
- 가운데 계층의 노트 수가 입력 값보다 적은 것이 특징
- 이런 구조로 입력 데이터를 압축하는 효과를 얻게 됨
- 이 과정에서 노이즈 제거에도 매우 효과적이라고 알려져 있음

오토인코더 핵심

- 입력층으로 들어온 데이터를 인코더를 통해 은닉층으로 내보냄
- 은닉층의 데이터를 디코더를 통해 출력층으로 내보냄
- 만들어진 출력값을 입력값과 비슷해지도록 만드는 가중치를 찾아내는 것

오토인코더 방식
- 변이형 (Variational AutoEncoder)
- 잡음제거 (De noising AutoEncoder)
"""

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("./mnist/data", one_hot=True)

# hyper parameter
learning_rate = 0.01  # 학습률
training_epoch = 20  # 전체 데이터를 학습할 총 횟수
batch_size = 100  # 한 번에 학습할 데이터(이미지)의 개수
n_hidden = 256  # 은닉층의 뉴런 개수
n_input = 28 * 28  # 입력값의 크기, 784

# 신경망 모델 구성
## 비지도 학습으로 Y 값이 없다.
X = tf.placeholder(tf.float32, [None, n_input])

# 인코더 구성
## 오토인코더의 핵심 모델 -> 인코더와 디코더를 만드는 것
## 인코더와 디코더를 만드는 방식에 따라 다양한 오토인코더를 만들 수 있음

W_encode = tf.Variable(tf.random_normal([n_input, n_hidden]))  # n_hidden 개의 뉴런을 가진 은닉층 만듦
b_encode = tf.Variable(tf.random_normal([n_hidden]))  # 가중치와 편향 변수를 원하는 뉴런의 개수만큼 설정

matmul = tf.matmul(X, W_encode)  # 입력값과 곱
add = tf.add(matmul, b_encode)  #
encoder = tf.nn.sigmoid(add)  # 활성화 함수

# 입력값인 n_input 값보다 n_hidden 값이 더 작다는 점.
# 입력값을 압축하고 노이즈를 제거하면서 입력값의 특징을 찾아내게 된다.

# 디코더 구성
W_decode = tf.Variable(tf.random_normal([n_hidden, n_input]))  # 입력값을 은닉층의 크기인 n_hidden 으로,
b_decode = tf.Variable(tf.random_normal([n_input]))  # 출력 값은 입력층의 크기인 n_input으로 만듦

decoder = tf.nn.sigmoid(tf.add(tf.matmul(encoder, W_decode), b_decode))

# 손실 함수 생성
# 가중치들을 최적화하기 위한 손실 함수 생성
# 기본적인 오코인코더의 목적: 출력값을 입력값과 가장 비슷하게 만드는 것
# 그렇게 하면 압축된 은닉층의 뉴런들을 통해 입력값의 특징을 알아낼 수 있다.

# 입력값 X를 평가하기 위한 실측값으로 사용
# 디코더가 내보낸 결과 값과의 차이를 손실값으로 설정
# 이 값의 차이는 거리 함수로 구한다.

cost = tf.reduce_mean(tf.pow(X - decoder, 2))

# 최적화 함수
# RMSPropOptimizer
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)

# 모델 학습

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(training_epoch):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)

        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs})

        total_cost += cost_val

    print('Epoch', '%04d' % (epoch + 1),
          'Avg. Cost = ', '{:.4f}'.format(total_cost / total_batch))

print("complete optimizer")

# result
sample_size = 10  # 총 10개의 테스트 데이터를 가져와 디코더를 이용해 출력값으로 만듦

samples = sess.run(decoder, feed_dict={X: mnist.test.images[:sample_size]})

# imshow()
# 위: 입력값의 이미지 출력
# 아래: 신경망으로 생성한 이미지 출력

fig, ax = plt.subplots(2, sample_size, figsize=(sample_size, 2))

for i in range(sample_size):
    ax[0][i].set_axis_off()
    ax[1][i].set_axis_off()

    ax[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))
    ax[1][i].imshow(np.reshape(samples[i], (28, 28)))

plt.show()