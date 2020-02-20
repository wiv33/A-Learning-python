import numpy as np

## 2*2 integer 다차원 배열을 초기화하지 않은 상태로 생성
np.empty((2, 3))

## X = np.array([[1,2,3],[4,5,6]],np.int32) 일 때,
# X와 동일한 shape를 가지는 배열을 초기화하지 않은 상태로 생성
X = np.array([[1,2,3], [4,5,6]], dtype='int32')
np.empty_like(X)


## 크기가 3인 단위행렬을 생성하세요
print(np.identity(3))

print(np.eye(3))


## 모든 원소가 1로 채워진 3*2 실수형 다차원 배열을 생성하세요.
print(np.ones((3, 2), dtype=float))

##
X = np.arange(4, dtype=np.int64)

print(np.ones_like(X))


## 모든 원소가 6으로 채워진 2*5 unit 형 다차원 배열 생성
np.full((2,5), 6, dtype=np.uint)

int_ = np.ones((2, 5), dtype=np.int) * 6
print(int_)

# 2, 4, 6, 8, ... 100
arange = np.arange(start=2, stop=101, step=2)
# print(arange)

# 3.0에서 10.0까지 50개의 원소가 균일하게 분포된 1차원 배열
linspace = np.linspace(start=3.0, stop=10.0, num=50)
print(linspace)