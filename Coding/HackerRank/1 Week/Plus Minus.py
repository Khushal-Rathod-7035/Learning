#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    plus_count = 0
    minus_count = 0
    zero_count = 0
    for i in arr:
        if i > 0:
            plus_count += 1
        elif i < 0:
            minus_count += 1
        else:
            zero_count += 1
    print("{0:.6f}".format(plus_count/total))
    print("{0:.6f}".format(minus_count/total))
    print("{0:.6f}".format(zero_count/total))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
