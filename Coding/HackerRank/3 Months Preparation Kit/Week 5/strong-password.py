#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    password_flag = [0, 0, 0, 0]
    for i in password:
        if i in numbers:
            password_flag[0] += 1
        elif i in lower_case:
            password_flag[1] += 1
        elif i in upper_case:
            password_flag[2] += 1
        elif i in special_characters:
            password_flag[3] += 1
        else:
            continue
    required_char = 0
    for i in password_flag:
        if i == 0:
            required_char += 1
    if n + required_char >= 6:
        return required_char
    else:
        required_char += (6 - (n + required_char))
        return required_char


if __name__ == '__main__':
    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
