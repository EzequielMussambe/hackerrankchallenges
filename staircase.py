import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for s in range(1,n+1):
        v = ("#"*s)
        if s==1:
            print(v.rjust(n))
        elif s> 1:
            print(v.rjust(n))
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
