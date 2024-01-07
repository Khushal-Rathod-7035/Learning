#!/bin/python3
import datetime
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    am_pm = s[-2:]
    if am_pm == 'AM':
        if s[:2] == '12':
            s = s.replace('AM', '')
            s = s.replace(s[:2], '00')
        else:
            s = s.replace('AM', '')
    else:
        if s[:2] == '12':
            s = s.replace('PM', '')
        else:
            new_hour = str(int(s[:2]) + 12)
            s = s.replace('PM', '')
            s = s.replace(s[:2], new_hour)
    print(s)

if __name__ == '__main__':
    s = input()
    timeConversion(s)
