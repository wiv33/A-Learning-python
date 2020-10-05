import tensorflow as tf

"""
과적합을 해결하는데 대표적인 방법
    
    Dropout

"""
inputs = tf.keras.layers.Input(shape=(20, 1))
output = tf.keras.layers.Dropout(rate=0.2)(inputs)
"""
Dropout().__init__()
:rate
    전체 입력 값에서 20%를 0으로 만든다.
    
:noise_shape
    정수형의 1D-tensor 값
    값을 지정하면 특정 값에 드롭아웃을 적용할 수 있다.
    이미지일 경우 특정 채널에만 드롭아웃을 적용할 수 있다.
    
:seed
    드롭아웃의 경우 지정된 확률 값을 바탕으로 무작위 드롭아웃을 적용하는데,
    이때 임의의 선택을 위한 값을 의미한다.
    같은 seed 값을 가지는 드롭아웃의 경우 동일한 드롭아웃 결과를 만든다.
    
    
tf.nn.dropout
0.2 : 80% 값을 0으로 만듦

"""

print(output)

inputs = tf.keras.layers.Input(shape=(20, 1))
dropout = tf.keras.layers.Dropout(rate=0.2)(inputs)
hidden = tf.keras.layers.Dense(10, activation=tf.nn.swish)(dropout)
output = tf.keras.layers.Dense(2, activation=tf.nn.sigmoid)(hidden)

print(output)
