from multiprocessing import Pool
import numpy as np


def my_func(a):
    print(type(a))
    return a, a


arr = np.zeros((10000,))

if __name__ == '__main__':
    pool = Pool(5)
    result = pool.map(my_func, np.split(arr, 5))
    pool.close()
    pool.join()
    print(np.array(result).shape)
    print(list(result))
