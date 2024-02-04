#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    all_s = {}
    for i in s:
        if i in all_s:
            all_s[i] += 1
        else:
            all_s[i] = 1
    all_key = len(list(all_s.keys()))
    all_sum = sum(list(all_s.values()))
    high_count = 0
    for i in all_s.values():
        all_count = list(all_s.values()).count(i)
        if all_count > high_count:
            high_count = i
    same_val = [i for i in all_s if all_s[i] == high_count]
    not_same_val = [i for i in all_s if i not in same_val]
    if len(same_val) == all_key:
        return 'YES'
    else:
        sum_same_val = sum([all_s[i] for i in all_s if i in same_val])
        sum_not_same_val = sum([all_s[i] for i in all_s if i in not_same_val])
        if len(not_same_val) == 1 and ((sum_not_same_val - high_count == 1) or sum_not_same_val ==1):
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result)
