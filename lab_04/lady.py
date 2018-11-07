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
        i = -1
        for letter in b:
            if letter == b[i+1] or letter == b[i-1]:
                i += 1
            elif letter != b[i+1]:
                return "NO"
        return "YES"
    elif "_" in b:
        b = b.replace("_", "")
        if len(b) <= 1:
            return "NO"
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
print(happyLadybugs("BBRRXX"))
print(happyLadybugs("BRBRXX"))