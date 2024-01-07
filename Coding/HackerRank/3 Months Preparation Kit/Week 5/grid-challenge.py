#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    len_grid = len(grid)
    len_col = len(grid[0])
    for i in range(len_grid):
        grid[i] = ''.join(sorted(grid[i]))
    columns = []
    for i in range(len_col):
        current_col = ''
        for j in range(len_grid):
            current_str = grid[j]
            current_col += current_str[i]
        columns.append(current_col)
    return_flag = True
    for i in columns:
        if i == ''.join(sorted(i)):
            continue
        else:
            return_flag = False
            break
    if return_flag:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)
