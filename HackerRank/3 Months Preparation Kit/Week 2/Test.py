#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    sumA = 0
    for i in range(row // 2):
        for j in range(col // 2):
            r1, r2 = i, row - i - 1
            c1, c2 = j, col - j - 1

            sumA += max(max(matrix[r1][c1], matrix[r1][c2]), max(matrix[r2][c1], matrix[r2][c2]))
    return sumA

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(result)

