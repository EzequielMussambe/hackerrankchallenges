 
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maxV =  max(arr)
    minV = min(arr)
    max_index = arr.index(maxV)
    min_index = arr.index(minV)

    arr[max_index] = 0
    minVal = sum(arr)
    arr[max_index] = maxV
    arr[min_index] = 0
    maxVal = sum(arr)
    print("{} {}".format(minVal, maxVal))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
