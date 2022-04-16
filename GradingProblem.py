#!/bin/python3
#Question -> https://www.hackerrank.com/challenges/grading/problem
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
    # Write your code here
    results = []
    for grade in grades:
        next_multiple5 = 5 * math.ceil(grade/5)
        
        if grade < 38 or next_multiple5 - grade >= 3:
            results.append(grade)
        else:
            results.append(next_multiple5)
       
    return results
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
