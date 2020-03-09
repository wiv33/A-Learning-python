"""
ref: _000_Boston_dataset

학습과정
    1. 데이터 입력을 위한 플레이스홀더 정의
    2. 학습에 사용할 파라미터를 변수형으로 정의
    3. 모델, 손실함수, 최적화함수 정의
    4. 세션 시작
    5. 변수 초기화 선언
    6. 데이터 피딩
    7. 최적화함수 실행

    *시각화
"""
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt  # 학습 결과 플롯용 패키지
from sklearn import datasets

boston = datasets.load_boston()
boston_slice = [x[5] for x in boston.data]

# 텐서플로에서 사용할 크기로 조정
# reshape 함수로 데이터를 열이 1인 배열형으로 변환
data_x = np.array(boston_slice).reshape(-1, 1)  # == np.array(boston_slice).reshape(506, 1)
data_y = boston.target.reshape(-1, 1)
# data_x.shape == data_y.shape: True

""" 
선형 회귀
    y = wx + b
    입력 데이터(x) * 기울기(w) + 편향(b, 절편이라고도 한다) = 타깃 데이터(y)가 되는 
    기울기와 편향을 찾는 것이 목표 
    
학습 전에는 기울기와 편향을 알 수 없기 때문에 0으로 설정한 후 최적화를 통해 학습한다.
"""

# 입력 데이터의 샘플 수를 얻는다.
n_sample = data_x.shape[0]

# 샘플 수 x 피처 수의 플레이스홀더.
# 피처를 하나만 사용하므로 피처 수는 1
X = tf.placeholder(tf.float32, shape=(n_sample, 1), name="X")

# 샘플 수 y 타깃 수의 플레이스홀더.
# 타깃 수가 집값 하나이므로 1이다.
y = tf.placeholder(tf.float32, shape=(n_sample, 1), name='y')

# 기울기. 피처 수 X 타깃 수의 크기를 가진다. 피처 수와 타깃 수가 1이므로 기울기는 1*1로 정의된다.
W = tf.Variable(tf.zeros((1, 1)), name="weights")

# 편향.
# 타깃 수 X 타깃 수의 크기를 가진다. 타깃 수가 1이므로 기울기는 1*1로 정의
b = tf.Variable(tf.zeros((1,1)), name="bias")

# => 학습함수, 손실함수, 최적화 함수 정의
"""
학습함수: 입력데이터 * 기울기 + 편향
손실함수: (타깃값 - (입력데이터 * 기울기 + 편향))^2 / 샘플 수 """

# 임력 데이터와 기울기의 곱을 구하기 위해 matmul,
# 제곱값을 구하기 위해 square,
# 모든 샘플에서의 제곱손실값을 더한 후 평균을 내기 위해 tf.reduce_mean 사용.

"""
matmul(a,b, transpose_a=False, transpose_b=False, 
    adjoint_a=False, adjoint_b=False,
    a_is_sparse=False, b_is_sparse=False, 
    name=None
)
a: 다차원 행렬
b: 다차원 행렬

a*b
a와 b의 행렬이 같아야 한다.
"""

"""
square(x, name=None)

x: 입력 텐서. type: half, float32, 64, int32, 64, complex64, 128
name: 연산명 
"""

"""
reduce_mean(input_tensor, axis=None, keep_dims=False, name=None, reduction_indices=None)

input_tensor: 입력텐서. numeric type
axis: 줄일 차원의 인덱스 값. 
    None일 경우 전 차원을 줄인다.
    0일 경우 각 행마다 평균을 계산하고
    1일 경우 각 열마다 계산
keep_dims: True일 경우 줄인 차원의 인덱스를 기억한다.
name: 연산명

@deprecated
reduction_indices: axis의 옛 이름
"""

"""최적화 방법 -> 경사하강법 최적화 클래스
tf.train.GradientDescentOptimizer.__init__(learning_rate, use_locking=False, name='GradientDescent')

경사하강법 외 최적화 클래스
AdaGrad(tf.train.AdagradOptimizer)
Adam(tf.train.AdamOptimizer)
"""
