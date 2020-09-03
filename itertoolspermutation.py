# Itertools.permutation -> https://www.hackerrank.com/challenges/itertools-permutations/problem?h_r=next-challenge&h_v=zen

from itertools import permutations

name, num = input().split()
num = int(num)


myList = list(permutations(name, num))
myList.sort()

for i in myList:
    name1 = "".join(i)
    print(name1)
