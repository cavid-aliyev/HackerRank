# Itertools.product() -> https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product


a = list(map(int, input().split()))
b = list(map(int, input().split()))

prod = list(product(a,b))


for n in prod:
  print(n, end=" ") # "end" bizim outputu bir line ustunde yazilmasi ucun lazimdir