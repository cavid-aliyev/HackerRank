#Set symmetric difference -> https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


a = int(input())
set1 = set(input().split())

b = int(input())
set2 = set(input().split())

print(len(set1.symmetric_difference(set2)))