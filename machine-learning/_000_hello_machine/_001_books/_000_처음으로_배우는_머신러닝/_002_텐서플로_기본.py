import tensorflow as tf

ta = tf.zeros((2, 2))
"""zeros(shape, dtype=tf.float32, name=None)
:shape
    리스트 혹은 1차원 정수 텐서. 생성할 텐서의 크기
    
:dtype
    데이터 타입

:name
    연산 명
"""
# result
# Tensor("zeros:0", shape=(2, 2), dtype=float32)