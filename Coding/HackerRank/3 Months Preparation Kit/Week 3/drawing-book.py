#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    mid = n // 2
    diff_page = n - p
    if p == 1 or (n / p == 1):
        return 0
    if n % 2 == 0:
        if diff_page >= mid:
            return p // 2
        else:
            if p % 2 == 0:
                return diff_page // 2
            else:
                return diff_page // 2 + 1
    else:
        if diff_page > mid:
            return p // 2
        else:
            return diff_page // 2

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
