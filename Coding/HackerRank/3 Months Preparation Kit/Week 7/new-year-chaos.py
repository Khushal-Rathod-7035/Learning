#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    min_val = float('inf')
    second_min_val = float('inf')

    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        if q[i] > min_val and q[i] > second_min_val:
            bribes += 2
        elif q[i] > min_val:
            bribes += 1

        if q[i] < min_val:
            second_min_val = min_val
            min_val = q[i]
        elif q[i] < second_min_val:
            second_min_val = q[i]

    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
