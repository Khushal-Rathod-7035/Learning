#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    sorted_arr = []
    length = len(arr)
    for _ in range(length):
        sorted_arr.append([])
    for i in range(length):
        if i < length // 2:
            sorted_arr[int(arr[i][0])].append('-')
        else:
            sorted_arr[int(arr[i][0])].append(arr[i][1])
    final_str = ''
    for i in sorted_arr:
        final_str += (' '.join(i) + ' ')
    print(final_str.strip())


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
