#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    if max(arr) > 100:
        length = max(arr) + 1
    else:
        add = 100 - max(arr)
        length = max(arr) + add
    frequncy_array = [0 for i in range(length)]
    for i in arr:
        frequncy_array[i] += 1
    return frequncy_array


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

