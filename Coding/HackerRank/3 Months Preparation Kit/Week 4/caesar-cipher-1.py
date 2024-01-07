#!/bin/python3

import math
import os
import random
import re
import string
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    if k >= 26:
        k = k % 26
    all_char_lower = string.ascii_lowercase
    all_char_upper = string.ascii_uppercase
    encrypted_string = ''
    for i in s:
        if i.isupper():
            i_index = all_char_upper.index(i) + k
            if i_index > 25:
                i_index = i_index % 25 - 1
            encrypted_string += all_char_upper[i_index]
        elif i.islower():
            i_index = all_char_lower.index(i) + k
            if i_index > 25:
                i_index = i_index % 25 - 1
            encrypted_string += all_char_lower[i_index]
        else:
            encrypted_string += i
    return encrypted_string


if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
