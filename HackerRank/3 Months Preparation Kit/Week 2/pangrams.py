#!/bin/python3

import math
import os
import random
import re
import string
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    all_char = list(string.ascii_lowercase)
    s = s.lower()
    for i in s:
        if i in all_char:
            all_char.remove(i)
        else:
            continue
    if len(all_char) > 0:
        return 'not pangram'
    else:
        return 'pangram'

if __name__ == '__main__':

    s = input()

    result = pangrams(s)

    print(result)
