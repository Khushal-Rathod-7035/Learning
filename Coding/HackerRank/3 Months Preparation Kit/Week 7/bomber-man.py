#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
def bomb_explode(grid):
    len_grid = len(grid)
    len_grid_ele = len(grid[0])
    full_grid = grid.copy()
    for i in range(len_grid):
        full_grid[i] = list(full_grid[i])
        for j in range(len_grid_ele):
            full_grid[i][j] = 'O'
    for i in range(len_grid):
        for j in range(len_grid_ele):
            if grid[i][j] == 'O':
                full_grid[i][j] = '.'
                if i+1 < len_grid:
                    full_grid[i + 1][j] = '.'
                if i-1 != -1:
                    full_grid[i - 1][j] = '.'
                if j+1 < len_grid_ele:
                    full_grid[i][j + 1] = '.'
                if j-1 != -1:
                    full_grid[i][j - 1] = '.'
    for i in range(len_grid):
        grid[i] = ''.join(full_grid[i])
    return grid


def bomberMan(n, grid):
    print(grid)
    if n <= 1:
        return grid
    if n % 2 == 0:
        for i in range(len(grid)):
            output = ''
            for j in range(len(grid[0])):
                output += 'O'
            grid[i] = output
        return grid
    elif n % 4 == 3:
        return bomb_explode(grid)
    elif n % 4 == 1:
        return bomb_explode(bomb_explode(grid))


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    for i in result:
        print(i)
