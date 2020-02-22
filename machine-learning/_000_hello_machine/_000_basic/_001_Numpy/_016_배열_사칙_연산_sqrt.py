import numpy as np

"""다차원 배열 연산 시 shape가 맞아야 연산이 된다.
요소별 합, 차, 곱, 나눗셈의 경우 shape 일치해야 한다.
(2,2), (2,2)
"""

x = np.array([[1., 2.], [3., 4.]])
y = np.array([[5., 6.], [7., 8.]])

"""요소의 합
"""
x + y
np.add(x, y)
# result
# array([[ 6.,  8.],
#        [10., 12.]])

"""요소의 차
"""
x - y
np.subtract(x, y)
# result
# array([[-4., -4.],
#        [-4., -4.]])

"""요소의 곱
"""
x * y
np.multiply(x, y)
# result
# array([[ 5., 12.],
#        [21., 32.]])

"""요소의 나눗셈
"""

x / y
np.divide(x, y)
# result
# array([[0.2       , 0.33333333],
#        [0.42857143, 0.5       ]])

"""요소의 제곱근
"""
np.sqrt(x)
# result
# array([[1.        , 1.41421356],
#        [1.73205081, 2.        ]])


