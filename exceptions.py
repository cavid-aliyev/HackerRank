# Exceptions -> https://www.hackerrank.com/challenges/exceptions/problem

say = int(input())
for i in range(say):
    try:
        eded1,eded2 = map(int,input().split())
        print(eded1//eded2)
    except Exception as f:
        print("Error Code:", f)
