import tensorflow as tf
from tensorflow import keras

"""
conv1d filtering
    가로 방향으로만 옮겨가면서 입력값에 대해 합성곱을 수행한다.
    연산 결과들이 모여서 최종 출력 값이 나오며,
    출력 값은 1차원 벡터가 된다.
   
Flatten 느낌 
"""

# Dense와 다른 점은 합성곱 연산을 수행하는 필터와 관련된 부분이 추가된 점.
# 합성곱은 필터의 크기를 필요로 하나, Conv1D는 필터의 높이(high)는 필요하지 않다.

# input = (5,10)
# kernel_size = 2
# filter = 10
#  ---
# output = (1, 4, 10)

# 필터의 크기가 5일 경우 1, 5, 10일까?

INPUT_SIZE = (5, 10)

inputs = tf.keras.layers.Input(shape=INPUT_SIZE)
dropout = tf.keras.layers.Dropout(rate=0.3)(inputs)
output = tf.keras.layers.Conv1D(filters=10,
                                kernel_size=3,
                                padding='same',
                                activation=tf.nn.relu)(dropout)
print(output)
