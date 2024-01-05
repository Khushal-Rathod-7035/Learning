#!/bin/python3

import math
import os
import random
import re
import sys


def closestNumbers(arr):
    arr.sort()
    min_value = 10**20
    new_array = []
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] <= min_value:
            min_value = arr[i+1] - arr[i]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] <= min_value:
            new_array += [arr[i], arr[i+1]]
    return new_array


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(result)
