#!/bin/python3
#question=>https://www.hackerrank.com/challenges/counting-valleys/problem
import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = {'U':1 , 'D':-1}
    sea_level = 0
    valleyCount = 0
    for step in path:
        sea_level += altitude[step]
        if sea_level == 0 and step =='U':
            valleyCount += 1
    return valleyCount
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
