# Input() -> https://www.hackerrank.com/challenges/input/problem

input1=list(map(int,input().split()))  #verilenleri list sheklinde yilir

x=input1[0]
y=input1[1]

result = input()
print(y==eval(result))