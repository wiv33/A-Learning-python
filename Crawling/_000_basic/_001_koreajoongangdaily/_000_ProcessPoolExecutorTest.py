import concurrent.futures
import numpy as np
from concurrent.futures import ProcessPoolExecutor
import os


def ps_print(x):
    return print(__name__, os.getpid(), x ** 3)


if __name__ == '__main__':
    PRIMES = np.arange(0, 7)
    with ProcessPoolExecutor(max_workers=7) as executor:
        executor.map(ps_print, PRIMES)
