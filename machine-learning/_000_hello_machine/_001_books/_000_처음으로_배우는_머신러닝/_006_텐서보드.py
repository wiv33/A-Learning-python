"""
텐서보드:
    연산 그래프와 파라미터를 시각화하여 학습 과정을 모니터링하거나
    디버깅하는 데 도움을 준다.

흐름
    1. 그래프 생성 -> FileWriter(생성한 그래프)
    2. tf.scalar_summary 클래스에 추적하고 싶은 값(ex.각 학습 시의 손실)을 인자로 갖는
    기록함수를 생성하고, 세선이 시작된 후 SummaryWriter 함수에 그 함수를 인자로 넣어 기록하는 방법

결과 출력
     텐서보드를 호출
     terminal
        tensorboard --logidr=./logs/fit
"""

import tensorflow as tf

session = tf.InteractiveSession()
a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
x = tf.add(a, b)
writer = tf.summary.FileWriter('./logs/fit', session.graph)
session.run(x)
writer.close()
session.close()
