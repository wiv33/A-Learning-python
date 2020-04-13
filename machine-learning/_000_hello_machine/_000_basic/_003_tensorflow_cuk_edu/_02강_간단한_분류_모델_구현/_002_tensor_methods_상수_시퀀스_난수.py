"""tensorflow methods 정리"""

import tensorflow as tf


tf.zeros(shape, dtype=dtypes.float32, name=None)
"""
모든 원소의 값이 0인 텐서 생성
:shape
    정수 리스트 또는 int32 타입의 1 - Dimension Tensor
:dtype
    반환되는 텐서의 원소 타입
:name
    [optional] 연산의 명칭
:return
    모든 원소가 0인 텐서
"""

tf.zeros_like(tensor, dtype=None, name=None, optimize=True)
"""
어떤 텐서를 입력값으로 받아 같은 타입과 shape를 가진 텐서 생성

:tensor
    입력 텐서
:dtype
    반환되는 텐서 타입
:name
    [optional] 연산의 명칭
:return
     모든 원소의 값이 0인 텐서 생성
"""

tf.one(shape, dtype=tf.float32, name=None)
"""
모든 원소의 값이 1인 텐서 생성
"""

tf.ones_like(tensor, dtype=None, name=None)
"""
모든 원소의 값이 0인 텐서 생성(입력 받는 텐서)
:dtype
    반환되는 텐서 타입
"""

tf.fill(dims, value, name=None)
"""
스칼라 값으로 채워진 텐서 생성
:dims
    int32 값의 텐서
:value
    스칼라 값
:name
    [optional] 연산의 명칭
"""

tf.linspace(start=, stop=, num=, name=None)
"""
구간 사이의 값들을 생성
:start
    float2 or float64 타입의 텐서 구간 시작 첫 번째 엔트리
:stop
    마지막 엔트리
:num
    구간 사이의 개수
"""

tf.range(start=, limit=None, delta=1, name='range')
"""
정수 시퀀스를 생성
:start
    시작 값
:limit
    마지막 값
:delta
    생성 배수
"""

tf.random_normal(shape=, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
"""
:mean
    정규 분포의 평균값
    0 - D 텐서 또는 dtype 타입의 파이썬 값
:stddev
    정규 분포의 표준편차
    0 - D 텐서 또는 dtype 타입의 파이썬 값
:dtype
    반환 값의 타입
:seed
    파이썬 정수

:return
    :shape 형태의 정규 난수 값들로 채워진 텐서 
"""

tf.truncated_normal(shape=, mean=0,0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
"""
절단 정규 분포로부터의 난수 값을 반환함.
"""

tf.random_uniform(shape=, minval=0, maxval=None, dtype=tf.float32, seed=None, name=None)
"""
균등분포로부터의 난수 값을 반환함
:minval
    난수값 생성 구간의 하한
    0 - D 텐서 또는 dtype 타입의 파이썬 값
:maxval
    난수값 생성 구간의 상한
    0 - D 텐서 또는 dtype 타입의 파이썬 값

:return
    :shape 형태의 균등 난수 값들로 채워진 텐서
"""

# shuffle - 혼함
tf.random_shuffle(value=, seed=None, name=None)
"""
값의 첫 번째 차원을 기준으로 랜덤하게 섞어준다.
:value
    섞기 위한 텐서
"""

tf.random_crop(value=, size=, seed=None, name=None)
"""
텐서를 주어진 사이즈만큼 랜덤하게 잘라낸다.
"""

tf.multinomial(logits=, num_samples=, seed=None, name=None)
"""
다항분포로부터 샘플을 추출한다.
"""

tf.set_random_seed(seed=)
"""그래프 수준의 난수 시드를 설정한다. """