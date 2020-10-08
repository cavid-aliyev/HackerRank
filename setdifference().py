# Set.difference() -> https://www.hackerrank.com/challenges/py-set-difference-operation/problem

a = int(input())
mySet = set(map(int, input().split()))

b = int(input())
mySet2 = set(map(int, input().split()))


#Total students
print(len(mySet - mySet2))