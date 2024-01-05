#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    if len(arr) < len(brr):
        for i in arr:
            if i in brr:
                brr.remove(i)
        brr = list(set(brr))
        brr.sort()
        return brr
    else:
        for i in brr:
            if i in arr:
                arr.remove(i)
        arr = list(set(arr))
        arr.sort()
        return arr


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(result)
