# Concatenate -> https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

a, b, c =  [int(i)
              for i in input().split()]


array1 = numpy.array([input().split()
                        for i in range(a)], int)


array2 = numpy.array([input().split()
                        for j in range(b)], int)


print(numpy.concatenate((array1, array2), axis=0))
