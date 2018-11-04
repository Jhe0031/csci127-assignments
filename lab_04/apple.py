#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    amount_apples = 0
    amount_oranges = 0
    
    for int in apples:
        if int + a >= s and int + a <= t:
            amount_apples += 1
        else:
            amount_apples += 0
    print('Apples:', amount_apples)
    for int in oranges:
        if int + b >= s and int + b <= t:
            amount_oranges += 1
        else:
            amount_apples += 0
    print('Oranges:', amount_oranges)

print(countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6, 5]))
print(countApplesAndOranges(8, 12, 6, 14, [2, -2, -1], [-5, 6, -5]))
print(countApplesAndOranges(2, 3, 1, 5, [-2], [-1]))