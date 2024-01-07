#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    current_level = 0
    valleys = 0
    valley_flag = False
    for location in path:
        if location == 'D':
            current_level -= 1
        else:
            current_level += 1
        if current_level < 0:
            valley_flag = True
        if valley_flag and current_level >= 0:
            valleys += 1
            valley_flag = False
    return valleys

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)

