# Given a base-10 integer, n, convert it to binary (base-2). 
# Then find and print the base-10 integer denoting the maximum number of consecutive 's in n's binary representation. 
# When working with different bases, it is common to show the base as a subscript.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # Binary in Python starting with 0b...
    # Starting from 2 means that it starts after the 0b
    bin_n = bin(n)[2:]
    
    # Convert the binary to a list
    binary_list = list(bin(n)[2:])
    
    # Create a new list
    new_list = []
    
    # Split the binary list on the number 0
    # Followed by appending the length of grouped 1s
    for x in ''.join(binary_list).split('0'):
        new_list.append(len(x))
        
    # Print the maximum value found in new_list
    print(max(new_list))
