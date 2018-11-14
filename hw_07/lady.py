# Copy of lady.py
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    b = b.upper()
    if "_" not in b:
        i = 0
        for letter in b:
            if letter == b[i+1]:
                if i+1 >= len(b)-1:
                    return "YES"
                else:
                    i += 1
            elif letter == b[i-1] and i < len(b):
                if i+1 >= len(b)-1:
                    return "YES"
                else:
                    i += 1
            elif letter != b[i+1] and i < len(b):
                return "NO"
            elif i >= len(b):
                return "YES"
        return "YES"
    elif "_" in b:
        b = b.replace("_", "")
        if len(b) <= 1:
            return "NO"
        else:
            count = {}
            for letter in b:
                count[letter] = 0
                i = 0
                while i < len(b):
                    if b[i] == letter:
                        count[letter] = count[letter]+1
                    i += 1
                if count[letter] < 2:
                    return "NO"
                elif count[letter] >= 2:
                    continue
        return "YES"
    
cases = ["RBY_YBR", "X_Y__X", "B_RRBR", "BBRRXX", "BRBRXX"]
for test in cases:
    print(happyLadybugs(test))