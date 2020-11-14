# Polynomials -> https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy

myList = list(map(float, input().split())) # take first float elements
oneElement = int(input())

arr = numpy.array(myList)

print(numpy.polyval(arr, oneElement))