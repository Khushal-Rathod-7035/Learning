#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    new_array = []
    len_array = []
    flag = True
    for i in range(len(a) - 1):
        if a[i+1] - a[i] <= 1:
            if flag:
                first_value = a[i]
                flag = False
            if a[i] - first_value <= 1 and a[i+1] - first_value <= 1:
                new_array.append(a[i])
                if i + 1 == len(a) - 1:
                    new_array.append(a[i+1])
            else:
                new_array.append(a[i])
                len_array.append(len(new_array))
                new_array = []
                flag = True
        else:
            new_array.append(a[i])
            len_array.append(len(new_array))
            new_array = []
            flag = True
    len_array.append(len(new_array))
    return max(len_array)

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
