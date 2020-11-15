# Set Mutation -> https://www.hackerrank.com/challenges/py-set-mutations/problem

input()

a = set(input().strip().split(" "))

for _ in range(int(input().strip())):
    arr = input().strip().split(" ")
    b = set(input().strip().split(" "))
    eval("a.{0}(b)".format(arr[0]))
l = []

for i in a:
    l.append(int(i))

print(sum(l))
