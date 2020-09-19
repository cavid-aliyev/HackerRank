# Symmetric Differences -> https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
firstSet = set(map(int, input().split(" ")))

N = int(input())
secondSet = set(map(int, input().split(" ")))

#sortluyub aralarindaki simmetrik ferqi tapaq
s = sorted(firstSet.symmetric_difference(secondSet))

for item in s:
    print(item)
