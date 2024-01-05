#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    minimum = 0
    maximum = 0
    min_flag = 0
    max_flag = 0
    first_iterate = True
    for i in scores:
        if first_iterate:
            minimum = i
            maximum = i
            first_iterate = False
            continue
        if i > maximum:
            max_flag += 1
            maximum = i
            continue
        if i < minimum:
            min_flag += 1
            minimum = i
    return max_flag, min_flag

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
