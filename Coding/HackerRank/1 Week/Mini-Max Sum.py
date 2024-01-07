#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total = []
    for i in range(len(arr)):
        sub_total = 0
        for j in range(len(arr)):
            if i != j:
                sub_total += arr[j]
        total.append(sub_total)
    print(str(min(total)) + "  " + str(max(total)))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
