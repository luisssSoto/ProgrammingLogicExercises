"""Sherlock and Squares"""

import math

def squares(a, b):
    begin = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    return end - begin + 1

# testcase 1.
a1 = 3
b1 = 9
print(squares(a1, b1))