# Collection deque -> https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
d = deque()
n = int(input())
for i in range(n):
    l = input().split()
    command = l[0]
    if len(l) > 1:
        e = l[1]
    if command == "append":
        d.append(e)
    elif command == "pop":
        d.pop()
    elif command == "appendleft":
        d.appendleft(e)
    elif command == "popleft":
        d.popleft()

print(*d)