from multiprocessing import Pool
import os
import numpy as np
from concurrent.futures import ProcessPoolExecutor


def multi_executor(args):
    os.system('python _003_download_four_numbers.py')


if __name__ == '__main__':
    PRIMES = np.arange(0, 10000)
    with ProcessPoolExecutor(max_workers=12) as executor:
        executor.map(multi_executor, PRIMES)
