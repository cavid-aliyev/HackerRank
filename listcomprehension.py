# List comprehensions - https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    myList = list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k!=n): # sertde deyilirdiki ijk nin cemi n e beraber olmamalidir.
                    myList.append([i,j,k])

print(myList)
