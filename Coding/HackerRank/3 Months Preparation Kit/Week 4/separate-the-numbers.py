#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    added_string = ''
    for i in range(len(s)-1):
        if int(s[i]) + 1 == int(s[i+1]):
            added_string += s[i]
            if len(s) - 2 == i:
                added_string += s[i+1]
                break

    print(added_string)


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
