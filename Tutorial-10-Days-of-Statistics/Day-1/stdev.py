# Given an array, arr, of n integers, calculate and print the standard deviation. 
# Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). 
# An error margin of  will be tolerated for the standard deviation.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mean(arr):
    n = len(arr)
    total_arr = 0
    for i in range(n):
        total_arr += int(arr[i])
    return total_arr / n
    
def stdDev(arr):
    # Print your answers to 1 decimal place within this function 
    squared_dist = 0
    
    # Calculate std dev
    for i in range(n):
        squared_dist += (arr[i] - mean(arr)) ** 2
    
    print(round((squared_dist / n) ** (1/2), 1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
