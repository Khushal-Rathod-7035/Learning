#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import Counter





def migratoryBirds(arr):
    counter = dict(Counter(arr))
    counter = dict(sorted(counter.items(), key= lambda item: (-item[1], item[0])))
    max_count_element = list(counter.keys())[0]
    return max_count_element


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

