# Min and Max -> https://www.hackerrank.com/challenges/np-min-and-max/problem

from numpy import array as arr

num1, num2 = map(int, input().split())

elem = arr([input().split()
                    for _ in range(num1)], int)

print(elem.min(axis=1).max())