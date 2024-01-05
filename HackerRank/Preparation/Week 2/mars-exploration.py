#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    start_string = True
    middle_string = False
    last_string = False
    output = 0
    for i in s:
        if start_string:
            start_string = False
            middle_string = True
            if i == 'S':
                continue
            else:
                output += 1
        elif middle_string:
            middle_string = False
            last_string = True
            if i == 'O':
                continue
            else:
                output += 1
        elif last_string:
            last_string = False
            start_string = True
            if i == 'S':
                continue
            else:
                output += 1
        else:
            output += 1

    return output


if __name__ == '__main__':
    s = input()

    result = marsExploration(s)

    print(result)
