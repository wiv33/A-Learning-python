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
# The function accepts INTEGER_ARRAY box as parameter.
#

def get_minus_x(max_idx, box):
    # 1보다는 크고 target box보다는 작은 값
    return max(1, min(box[max_idx], sum(box) // len(box)))


def solution(box):
    # Write your code here

    ans = 0
    while True:
        max_idx, min_idx = choice_max_idx_tuple(box)
        minus_x = get_minus_x(max_idx, box)

        print(minus_x)
        box[max_idx], box[min_idx] = box[max_idx] - minus_x, box[min_idx] + minus_x

        # print(max_idx)
        # print(box[max_idx:max_idx - 1])



    return ans


def choice_max_idx_tuple(box):
    target = box.index(max(box[1:]))
    added = box.index(target - 1)
    return target, added


if __name__ == '__main__':
    box_count = int(4)

    box = [1, 5, 7, 6]

    result = solution(box)
    print(result)
