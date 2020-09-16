# Lists -> https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    myList = []
    for item in range(0, N):
        commandText = input()
        commandSplited = commandText.split(" ")
        if commandSplited[0] == "insert":
            myList.insert(int(commandSplited[1]), int(commandSplited[2]))
        elif commandSplited[0] == "print":
            print(myList)
        elif commandSplited[0] == "remove":
            num = int(commandSplited[1])
            myList.remove(num)
        elif commandSplited[0] == "append":
            num = int(commandSplited[1])
            myList.append(num)
        elif commandSplited[0] == "sort":
            myList.sort()
        elif commandSplited[0] == "pop":
            myList.pop()
        elif commandSplited[0] == "reverse":
            myList.reverse()
