#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numofPrizes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY marks
#

def numofPrizes(k, marks):
    marks.sort()
    print("sorted", marks)
    total_marks = 0
    curr_rank = 0
    curr_mark = marks[-1]
    while curr_rank < k and len(marks):
        curr_mark = marks.pop()
        curr_rank += 1
        if curr_mark:
            print(curr_mark)
            total_marks += 1
        if curr_rank == k:
            while len(marks) and curr_mark == marks[-1]:
                print("CURR", curr_mark)
                print("NEXT", marks[-1])
                if curr_mark:
                    print(curr_mark)
                    total_marks += 1
                curr_mark = marks.pop()
                
    return total_marks

numofPrizes(4, [2,2,3,4,5])
