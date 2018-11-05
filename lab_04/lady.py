#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    b = b.upper()
    b = b.replace("_", "")
    if len(b) <= 1:
        print("NO")
    else:
        for letter in b:
            i = 0
            count = 0
            while i < len(b):
                if b[i] == letter:
                    count += 1
                i += 1
            if count < 2:
                return "NO"
            elif count >= 2:
                continue
    return "YES"
print(happyLadybugs("RBY_YBR"))
print(happyLadybugs("X_Y__X"))
print(happyLadybugs("B_RRBR"))