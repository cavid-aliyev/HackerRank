# Inner and Outer -> https://www.hackerrank.com/challenges/np-inner-and-outer/problem?h_r=next-challenge&h_v=zen

import numpy

A=numpy.array(input().split(),int)
B=numpy.array(input().split(),int)

print(numpy.inner(A,B))
print(numpy.outer(A,B))
