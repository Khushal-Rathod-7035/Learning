#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        mid = len(s) // 2
        change_required = 0
        first = s[:mid]
        second = s[mid:]
        anagram_count = {}
        for i in first:
            if i in anagram_count:
                anagram_count[i] += 1
            else:
                anagram_count[i] = 1

        for i in second:
            if i in anagram_count and anagram_count[i] != 0:
                anagram_count[i] -= 1

        for value in anagram_count.values():
            change_required += value

    return change_required


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)
