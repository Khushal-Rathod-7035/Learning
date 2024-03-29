#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = []
    for _ in range(n):
        arr.append([])
    last_answer = 0
    answers = []
    for i in queries:
        idx = ((i[1] ^ last_answer) % n)
        if i[0] == 1:
            arr[idx].append(i[2])
        if i[0] == 2:
            last_answer = arr[idx][i[2]%len(arr[idx])]
            answers.append(last_answer)
    return answers


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)
