# Nested lists - https://www.hackerrank.com/challenges/nested-list/problem

marksheet = []
scoresheet = []
if __name__ == '__main__':

    for _ in range(int(input())): # telebelerin sayi
        ad = input() #telebenin adi
        qiymet = float(input()) #telebenin qiymeti
        marksheet+=[[ad, qiymet]]
        scoresheet+=[qiymet]
    x=sorted(set(scoresheet))[1]

    for n, s in sorted(marksheet):
        if s==x:
            print(n)
