# Plus minus -> https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    a = 0
    b = 0
    c = 0
    for i in range(n):
        if arr[i] > 0:
            a += 1
        elif arr[i] < 0:
            b += 1
        else:
            c += 1
    print(a / n)
    print(b / n)
    print(c / n)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
