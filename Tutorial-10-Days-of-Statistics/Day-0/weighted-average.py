# Given an array, X, of N integers and an array, , representing the respective weights of 's elements, 
# calculate and print the weighted mean of 's elements. 
# Your answer should be rounded to a scale of  decimal place (i.e.,  format).

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    total_val_times_weights = 0
    total_weights = 0
    for i in range(n):
        total_val_times_weights += X[i] * W[i]
        total_weights += W[i]
    print(round(total_val_times_weights/total_weights, 1))
        
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
