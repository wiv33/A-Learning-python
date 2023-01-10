#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER z
#

def solution(_x, _y, _z):
    # Write your code here

    x, y = min(_x, _y), max(_x, _y)
    if y - x > z:
        return -1

    k = x
    cnt = z

    while cnt > 2:
        if k == y:
            break
        cnt -= 1
        k += 1

    print(cnt // 2)
    if cnt > 2:
        k = k + cnt // 2
    else:
        k = k + cnt

    return k


if __name__ == '__main__':

    x = int(333)

    y = int(332)

    z = int(635)

    result = solution(x, y, z)

    print(result)