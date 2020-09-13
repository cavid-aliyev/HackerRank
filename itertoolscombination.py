# Utertools.combinations() -> https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

a, b = input().split()

print(*[''.join(k)

        for i in range(1, int(b) + 1)

        for k in combinations(sorted(a), i)],

      sep='\n')
