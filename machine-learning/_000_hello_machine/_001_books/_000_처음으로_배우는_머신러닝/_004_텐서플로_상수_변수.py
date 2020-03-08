import tensorflow as tf

"""변수 텐서

tf.Variable()
"""

W1 = tf.zeros((3, 3)) # 0 값의 3*3 행렬
W2 = tf.Variable(tf.zeros((2, 2)), name='weights') # 변수 텐서, 모든 요소값이 0인 2*2 행렬

# session = tf.InteractiveSession()
# print(W1.eval())
# print(W2.eval())

with tf.Session() as sess:
    """중요 포인트*
    텐서플로의 Variable()로 선언된 텐서들은
    global_variables_initializer()를 호출해야 사용할 수 있다.
    """
    sess.run(tf.global_variables_initializer())
    print(W1.eval())
    print(W2.eval())