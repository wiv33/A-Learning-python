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


def plot_graph(y, fout):
    """데이터 플롯을 위한 함수. 입력값(피처값), 출력값(집값)을 플롯한다."""

    plt.scatter(data_x.reshape(1, -1)[0], boston.target.reshape(1, -1)[0])
    plt.plot(data_x.reshape(1, -1)[0], y.reshape(1, -1)[0])
    plt.savefig(fout)
    plt.clf()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # 텐서보드용 서머리 라이터를 위에 지정한 디렉터리와 그래프를 이용하여 생성
    summary_writer = tf.summary.FileWriter('./logs/fit', sess.graph)

    # 학습 전의 예측된 기울기 상태
    y_pred_before = sess.run(y_pred, {X: data_x})

    plot_graph(y_pred_before, 'before.png')

    # 최적화함수를 이용하여 기울기를 100번 업데이트
    for i in range(100):
        # loss 연산, summary_op 연산, train_op 연산
        #loss 연산의 결과를 loss_t,
        # summary_op 연산의 결과를 summary에 받는다.
        loss_t, summary, _ = sess.run([loss, summary_op, train_op], feed_dict={X: data_x, y: data_y})

        # 각 업데이트마다 생성된 summary_op 함수의 결과를 서머리 라이터에 작성
        summary_writer.add_summary(summary, i)

        if i % 10 == 0:
            print('loss = % 4.4f' % loss_t.mean()) # 10회 학습 후의 평균 손실
            y_pred_after = sess.run(y_pred, {X: data_x})

    y_pred_after = sess.run(y_pred, {X: data_x})
    plot_graph(y_pred_after, "after.png")
