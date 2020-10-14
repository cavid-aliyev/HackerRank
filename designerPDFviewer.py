# Designer PDF Viewer -> https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
   maxnum = 0
   for letter in word:
    maxnum = max(maxnum, h[ord(letter) - ord('a')])
   return maxnum*len(word)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
