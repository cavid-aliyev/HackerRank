# Collections.namedtuple() -> https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

import collections

n = int(input())
m = input()
total = 0
Telebeler = collections.namedtuple('Telebeler', m)
for _ in range(n):
    telebe = Telebeler(*input().split())
    total += int(telebe.MARKS)


print('{:.2f}'.format(total/n))