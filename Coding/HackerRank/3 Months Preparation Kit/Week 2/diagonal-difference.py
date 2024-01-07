#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonal = 0
    left_flag = 0
    for i in arr:
        left_diagonal += i[left_flag]
        left_flag += 1
    right_flag = len(arr) - 1
    right_diagonal = 0
    for i in arr:
        right_diagonal += i[right_flag]
        right_flag -= 1
        if right_flag < 0:
            break

    return abs(left_diagonal-right_diagonal)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
