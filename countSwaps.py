#!/bin/python3

import math
import os
import random
import re
import sys
#Question-> https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count_swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count_swaps += 1
            
    return f"Array is sorted in {count_swaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]} "
                

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(countSwaps(a))
