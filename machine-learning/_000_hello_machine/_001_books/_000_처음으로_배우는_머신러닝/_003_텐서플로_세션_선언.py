import tensorflow as tf
import numpy as np

ta = tf.zeros((2, 2))

# 세션을 사용하지 않고 텐서플로를 사용하면 에러 발생
# print(ta.eval())


"""모든 계산이 세션 안에서 실행:run() 또는 평가:eval() 함수로 호출되어야 한다는 것

:run()
    함수 호출
:eval()
    텐서 값 출력
"""


session = tf.InteractiveSession()
print(ta.eval())
session.close()
# result
# [[0. 0.]
#  [0. 0.]]

# np와 동일

zeros = np.zeros((2, 2))
print(zeros)
# result
# [[0. 0.]
#  [0. 0.]]

