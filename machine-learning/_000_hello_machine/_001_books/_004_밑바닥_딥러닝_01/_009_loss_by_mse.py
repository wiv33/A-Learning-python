import numpy as np


def mean_squared_error(y, t):
    minus = (y - t)
    squared = minus ** 2
    np_sum = np.sum(squared)
    result = 0.5 * np_sum
    return result


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [.1, .05, .1, .0, .05, .1, .0, .6, .0, .0]
(len(y), mean_squared_error(np.array(t), np.array(y)))

y = [.1, .05, .1, .0, .05, .1, .0, .0, .6, .0]
(len(y), mean_squared_error(np.array(t), np.array(y)))

y = [.1, .05, .6, .0, .05, .1, .0, .1, .0, .0]
(len(y), mean_squared_error(np.array(t), np.array(y)))
