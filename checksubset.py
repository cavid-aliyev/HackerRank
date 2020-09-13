# Check Subset -> https://www.hackerrank.com/challenges/py-check-subset/problem
for _ in range(int(input())):
    a = int(input())
    b = set(map(int, input().split()))
    c = int(input())
    d = set(map(int, input().split()))

    print(b & d == b)
