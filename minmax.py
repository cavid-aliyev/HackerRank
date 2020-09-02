# Min-Max sum -> https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sira = sorted(arr) # verilen massivin min, max larin cemini tapmaq ucun sort edekki, evvelki ve son reqemi cixmaq werti ile min ve maxlarin cemini tapaq
    print(sum(sira[:-1]), sum(sira[1:]))

    a = min(arr)
    b = max(arr)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
