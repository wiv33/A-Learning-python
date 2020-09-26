import tensorflow as tf

"""
W = tf.Variable(tf.random_uniform([5, 10], -1., 1.))
b = tf.Variable(tf.zeros([10]))

y = tf.matmul(W, x) + b
"""

# tf 1.x 방식을 Dense 객체로 변환
# dense = tf.keras.layers.Dense()
# output = dense(input)

# case 2
# output = tf.keras.layers.Dense()(input)

"""
Dense().__init__
    :units
     출력 값의 크기
     
    :activation
     활성화 함수
     
    :use_bias
     편향(b)을 사용할지 여부, Boolean 값
     
    :kernel_initializer
     가중치(W) 초기화 함수
     
    :bias_initializer
     편향 초기화 함수
     
    :kernel_regularizer
     가중치 정규화 방법
     
    :bias_regularizer
     편향 정규화 방법
    
    :activity_regularizer
     출력 값 정규화 방법
     
    :kernel_constraint
     Optimizer에 의해 업데이ㅡ된 이후에 가중 치에적용되는 부가적인 제약함수
     (ex. norm constraint, value constraint)
     
    :bias_constraint
     Optimizer에 의해 업데이트된 이후에 편향에 적용되는 부가적인 제약 함수
     (ex. norm constraint, value constraint)
     
"""

INPUT_SIZE = (20, 1)
inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
outputs = tf.keras.layers.Dense(units=10, activation=tf.nn.sigmoid)(inputs)


#


INPUT_SIZE = (20, 1)
inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
hidden = tf.keras.layers.Dense(units=10, activation=tf.nn.sigmoid)(inputs)
outputs = tf.keras.layers.Dense(units=2, activation=tf.sigmoid)(hidden)

print(outputs)