import numpy as np


def softmax(a):
    c = np.max(a)  # inf 방지로 line 로직 추가
    exp_a = np.exp(a - c)  # inf 방지로 (- c) 로직 추가
    # print("1", exp_a)
    sum_exp_a = np.sum(exp_a)
    # print("2", sum_exp_a)
    y = exp_a / sum_exp_a
    # print("3", y)
    return y


a = np.array([.3, 2.9, 4.])
# a = np.array([1010, 1000, 999])
res = softmax(a)
print(res)
# [0.01821127 0.24519181 0.73659691]
# 1.8%, 24.5%, 73.7%
assert sum(res) == 1.0

# softmax는 0~1.0 사이의 실수를 출력한다.
# 출력의 총 합은 1이다.
# 함수의 출력은 확률로 해석할 수 있다.
