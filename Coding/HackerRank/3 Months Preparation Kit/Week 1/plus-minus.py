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
    length = len(arr)
    positive_flag = 0
    negative_flag = 0
    zero_flag = 0
    for i in arr:
        if i > 0:
            positive_flag += 1
        elif i < 0:
            negative_flag += 1
        else:
            zero_flag += 1
    print(positive_flag/length)
    print(negative_flag/length)
    print(zero_flag/length)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
