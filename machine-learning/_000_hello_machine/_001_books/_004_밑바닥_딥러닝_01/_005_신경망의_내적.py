import numpy as np

X = np.array([1, 2])
assert X.shape == (2,)

W = np.array([[1, 3, 5], [2, 4, 6]])
assert W.shape == (2, 3)

Y = np.dot(X, W)
assert Y.shape == (3,)


# ====================================================


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 입력층 -> 1층 시작

X = np.array([1.0, .5])
assert X.shape == (2,)

W1 = np.array([[.1, .3, .5], [.2, .4, .6]])
assert W1.shape == (2, 3)

B1 = np.array([.1, .2, .3])
assert B1.shape == (3,)

dot = np.dot(X, W1)
assert np.array_equal(dot, [.2, .5, .8])

A1 = dot + B1
assert np.array_equal(A1, [.30000000000000004, .7, 1.1])

Z1 = sigmoid(A1)
assert Z1.shape == (3,)
# 입력층 -> 1층 끝

# 1층 -> 2층

W2 = np.array([[.1, .4], [.2, .5], [.3, .6]])
assert W2.shape == (3, 2)  # 이전 층의 입력 3, 다음 층의 출력 2

B2 = np.array([.1, .2])
assert B2.shape == (2,)  # 출력 2

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)


# 1층 -> 2층 끝

# 2층 -> 마지막
# 활성화 함수, 책에선 시그마로 표현
def identity_function(x):
    return x


W3 = np.array([[.1, .3], [.2, .4]])
B3 = np.array([.1, .2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)
print(Y)

# 출력층 활성화 함수는 풀고자 하는 문제의 성질에 맞게 정한다.
"""
    회귀: 항등함수
    2클래스 분류: 시그모이드
    다중 클래스 분류: 소프트맥스
"""