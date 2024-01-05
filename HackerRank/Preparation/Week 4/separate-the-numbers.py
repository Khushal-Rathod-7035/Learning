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
    n = len(s)
    for i in range(1, (n//2) + 1):
        first_num = s[:i]
        first_num = int(first_num)
        current = first_num
        flag = True
        j = i
        while j < n:
            second_num = int(current) + 1
            second_num = str(second_num)
            len_sec = len(second_num)
            real_second = s[j:j+len_sec]
            if second_num == real_second:
                j += len_sec
                current = second_num
                continue
            else:
                flag = False
                break
        if flag:
            return print('YES', first_num)
    return print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
