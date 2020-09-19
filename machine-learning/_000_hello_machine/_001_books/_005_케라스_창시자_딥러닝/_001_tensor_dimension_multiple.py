import numpy as np


def naive_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1

    assert x.shape[0] == y.shape[0]

    z = 0.
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z


def naive_matrix_vector_dot(x, y):
    assert len(x.shape) == 2
    assert len(x.shape) == 1

    assert x.shape[1] == y.shape[0]

    # 반환될 벡터
    z = np.zeros(x.shape[0])

    for i in range(x.shape[0]):
        # for j in range(x.shape[1]):
        #     z[i] += x[i, j] * y[j]
        z[i] = naive_vector_dot(x[i, :], y)
    return z


def naive_matrix_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]

    z = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x = x[i, ]
            column_y = y[:, j]
            z[i, j] = naive_vector_dot(row_x, column_y)

    return z

"""
벡터와 벡터의 점곱은 성립되나,
행렬과 벡터, 행렬과 행렬의 점곱 교환 법칙은 성립하지 않음
"""
