# Collections.OrderedDict() -> https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input())
myDict = OrderedDict()

for _ in range(n):
    ad, boshluq, qiymet = input().rpartition(' ')
    myDict[ad] = myDict.get(ad,0) + int(qiymet)
for ad, qiymet in myDict.items():
    print(ad, qiymet) 
