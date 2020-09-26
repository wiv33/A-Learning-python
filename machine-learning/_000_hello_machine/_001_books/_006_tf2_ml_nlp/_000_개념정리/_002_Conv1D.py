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

"""
tf.keras.layers.Conv1D().__init__()

:filters
    필터의 개수
    정수형으로 지정
    **출력의 차원 수를 나타냄**
kernel_size
strides
padding
data_format
dilation_rate
activation
use_bias
kernel_initializer
bias_initializer
kernel_regularizer
bias_regularizer
activity_regularizer
kernel_constraint
bias_constraint
"""