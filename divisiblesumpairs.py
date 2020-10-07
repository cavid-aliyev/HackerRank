#Divisible Sum Pairs -> https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    num = [i for i in range(n)]
    num = list(combinations(num, 2))
    total = 0
    for i in num:
        if i[0] < i[1] and (ar[i[0]]+ar[i[1]]) % k == 0:
            total += 1
    return(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
