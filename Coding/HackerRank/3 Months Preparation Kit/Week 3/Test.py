#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    max_val = max(max(a), max(b))
    all_factorial = []
    for i in range(1, max_val + 1):
        if max_val % i == 0:
            all_factorial.append(i)
    for i in b:
        all_factorial = [x for x in all_factorial if i % x == 0]
    for i in a:
        all_factorial = [x for x in all_factorial if x % i == 0]
    return all_factorial


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
