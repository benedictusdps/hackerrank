# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

# Given an array, values, of n integers and an array, freqs, representing the respective frequencies of values's elements, 
# construct a data set, S, where each values[i] occurs at frequency freqs[i]. Then calculate and print S's interquartile range, 
# rounded to a scale of 1 decimal place (i.e., 12.3 format).

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return ((arr[int((n-2)/2)] + arr[int(n/2)])/2)
    else:
        return arr[int((n-1)/2)]
        
def quartiles(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        Q1, Q3 = median(arr[:int(n/2)]), median(arr[int(n/2):])
    else:
        Q1, Q3 = median(arr[:int((n-1)/2)]), median(arr[int((n+1)/2):])
    return float(Q1), float(Q3)

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    new_arr = []
    for i in range(n):
        new_arr += [val[i]] * freq[i]
    new_arr.sort()
    
    interq = quartiles(new_arr)
    print(round(interq[1] - interq[0], 1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
