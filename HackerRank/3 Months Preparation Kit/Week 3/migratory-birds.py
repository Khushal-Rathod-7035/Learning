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

def migratoryBirds(arr):
    sightings = {}
    for i in arr:
        if i in sightings:
            sightings[i] += 1
        else:
            sightings[i] = 1

    max_value = 0
    max_values = {}
    for i in sightings:
        if max_value <= sightings[i]:
            max_value = sightings[i]
            max_values[i] = sightings[i]
    output = list(max_values.keys())
    output.sort()
    return output[0]


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)