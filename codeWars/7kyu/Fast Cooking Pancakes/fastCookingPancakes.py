import math

def cook_pancakes(n, m):
    if n <= m: totalTime = 2
    else:
        numberOfTimes = n / m
        totalTime = math.ceil(numberOfTimes * 2)
    return totalTime

1
121
12312
1234321
123454321

for i in range(5):
    print()