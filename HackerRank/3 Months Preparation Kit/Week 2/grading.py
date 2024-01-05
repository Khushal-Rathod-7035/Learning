#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_graded = []
    for i in grades:
        if i < 40:
            check_difference = 5 - (i % 5)
            if i < 38:
                rounded_graded.append(i)
            else:
                rounded_graded.append(i + check_difference)
        else:
            check_difference = 5 - (i % 5)
            if check_difference < 3:
                rounded_graded.append(i+check_difference)
            else:
                rounded_graded.append(i)
    return rounded_graded


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
