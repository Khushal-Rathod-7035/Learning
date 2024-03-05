#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        first_val = arr[i]
        for j in range(i+1, len(arr)):
            second_val = arr[j]
            if first_val + second_val == m:
                break
            else:
                continue
        if first_val + second_val == m:
            break
        else:
            continue
    return [i+1, j+1]


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(result)
