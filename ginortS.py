# ginortS -> https://www.hackerrank.com/challenges/ginorts/problem 



kicik = ""
boyuk = ""
tek = ""
cut = ""

string=sorted(input())


for n in string:

   if n.islower():
       kicik += n

   elif n.isupper():
       boyuk += n

   elif int(n) % 2 != 0:
       tek += n

   elif int(n) % 2 == 0:
       cut += n

print(kicik + boyuk + tek + cut)
