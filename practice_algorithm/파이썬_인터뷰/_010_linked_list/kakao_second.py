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
#  1. INTEGER_ARRAY cost
#  2. INTEGER x
#

def solution(cost, x):
    # Write your code here
    _cost = {v: i for i, v in enumerate(cost)}
    cost.sort(reverse=True)
    idx_groups = []
    print_groups = []
    for i in range(len(cost)):
        inner_idx_group = []
        inner_cost_group = []
        for j in range(len(cost)):
            if i == j:
                continue

            j_ = sum(inner_cost_group) + cost[j]
            if j_ <= x:
                inner_idx_group.append(_cost[cost[j]])
                inner_cost_group.append(cost[j])

        idx_groups.append(inner_idx_group)
        print_groups.append(inner_cost_group)

    print(idx_groups)
    ans = 0
    for idx_group in idx_groups:
        inner_max = 0
        for j in idx_group:
            j_1 = 2 ** j
            inner_max += j_1
        ans = max(ans, inner_max)

    return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(5)

    cost = [10, 20, 14, 40, 50]

    x = int(70)

    result = solution(cost, x)
    print("res = ", result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()