#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    new_str = list(s)
    while True:
        if len(new_str) <= 1:
            break
        current_str = new_str.copy()
        for i in range(len(new_str)-1):
            if new_str[i] == new_str[i+1]:
                new_str.pop(i)
                new_str.pop(i)
                break
        if current_str == new_str:
            break
    if len(new_str) == 0:
        return 'Empty String'
    return ''.join(new_str)


if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result)
