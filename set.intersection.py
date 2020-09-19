# Set.intersection -> https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

a = int(input())
firstSet = set(map(int, input().split()))
b = int(input())
secondSet = set(map(int, input().split()))

print(len(firstSet.intersection(secondSet)))
