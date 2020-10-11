#Incorrect Regex -> https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

for i in range(int(input())):
    a = True
    try:
        regex = re.compile(input())
    except re.error:
      a = False

    print(a)
