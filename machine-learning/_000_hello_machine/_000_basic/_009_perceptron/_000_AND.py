def AND():
    F = .0
    T = 1.
    bias = 1.
    X = [
        [F, F, bias],
        [F, T, bias],
        [T, F, bias],
        [T, T, bias],
    ]
    Y = [
        [F],
        [F],
        [F],
        [T]
    ]
    return X, Y


x, y = AND()
