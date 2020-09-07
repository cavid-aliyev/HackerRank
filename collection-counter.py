# Collection-counter -> https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

# Ölçülərin sayını əlavə edirik
mallarin_razmerlerinin_sayi= int(input("Ölçüləri sayını əlavə edin: "))

#Öıçüləri bir listə yığırıq
myList = Counter(list(map(int, input().split())))

#Mallarin db sinden satilan mallari yaziriq
satilan_mallarin_sayi = int(input("Satılan malları əlavə edin"))

myTuple = [tuple(map(int, input().split()))
           for i in range(satilan_mallarin_sayi)]

#Toplam satılan malların qiymətlərinin cəmi
cem = 0

for i in myTuple:
    if i[0] in myList:
        if myList[i[0]] > 0:
            cem += i[1]
    myList[i[0]] -= 1
print(cem)