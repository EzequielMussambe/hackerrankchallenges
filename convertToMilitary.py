#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    #s = s.split(":")
    s_ = s.split(":")
    if "AM" in s_[2]:
        
        if s_[0] == '12':
            morn_noon = "00:{}:{}".format(s_[1], s_[2][:2])
            
        elif s_[0] != '12':
            morn_noon = s[:8]
           
    elif "PM" in s_[2]:
        if s_[0] == '12':
            morn_noon = "12:{}:{}".format(s_[1], s_[2][:2])
            
        elif s_[0] != '12':
            add_time = int(s_[0]) + 12
            morn_noon = "{}:{}:{}".format(add_time,s_[1], s_[2][:2])
    
    return morn_noon  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
