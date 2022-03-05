# Given an array, arr, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). 
# It is guaranteed that Q1, Q2, and Q3 are integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        return int((arr[int((n-2)/2)] + arr[int(n/2)])/2)
    else:
        return arr[int((n-1)/2)]
        

def quartiles(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        Q1, Q2, Q3 = median(arr[:int(n/2)]), median(arr), median(arr[int(n/2):])
    else:
        Q1, Q2, Q3 = median(arr[:int((n-1)/2)]), median(arr), median(arr[int((n+1)/2):])
    return Q1, Q2, Q3
       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
