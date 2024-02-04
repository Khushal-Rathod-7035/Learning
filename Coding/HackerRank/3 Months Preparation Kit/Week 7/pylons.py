#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    plants = 0
    range_val = (k-1)*2 + 1
    i = 0
    while i < len(arr):
        if arr[(i + range_val)-k] == 1:
            plants += 1
            i += range_val
        else:
            return -1
    return plants


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(result)
