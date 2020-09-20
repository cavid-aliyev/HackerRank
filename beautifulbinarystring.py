# Beautiful binary string -> https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(myList):
    myList = list(myList)
    say = 0

    for i in range(n-2):
        if myList[i]=='0' and myList[i+1]=='1' and myList[i+2]=='0': #010
            say += 1
            myList[i+2] = '1'
    return say

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    myList = input()

    result = beautifulBinaryString(myList)

    fptr.write(str(result) + '\n')

    fptr.close()
