#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)

    zero_count = positive_c = negative_c = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        elif num < 0:
            negative_c += 1
        else:
            positive_c += 1

    z_res = zero_count/n
    print("{:.6f}".format(z_res))
    p_res = negative_c/n
    print("{:.6f}".format(p_res))
    n_res = negative_c/n
    print("{:.6f}".format(n_res))

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
