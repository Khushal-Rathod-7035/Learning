#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pairs = {}
    for i in range(n):
        if ar[i] in pairs:
            pairs[ar[i]] += 1
        else:
            pairs[ar[i]] = 1
    total_pairs = 0
    print(pairs)
    for i in pairs.values():
        if i >= 2:
            total_pairs += (i // 2)
    return total_pairs


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
