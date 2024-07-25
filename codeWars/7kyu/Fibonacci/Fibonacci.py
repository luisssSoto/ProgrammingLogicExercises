"""Fibonacci"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f1 = 0
        f2 = 1
        for i in range(n - 1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3
# 0 1 2 3 4 5 6
# 0+1=1
# 1+1=2
# 1+2=3
# 2+3=5
# 3+5=8
# 5+8=13
print(fibonacci(6))

#Dangerous because of time complexity
def fib(n):
    if n == 0:
        return 0
    elif n== 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(34))

'''1.
input: integer number
output: corresponding fibonacci number

2.
edge cases: 0 return 0, 1 return 1, since 2 starts the fibonacci behavior
f1 + f2 = result
for loop 
keeping track about the last two numbers
temp = f1, f1 = f2 and temp + f1 = f2

3.
conditional statement for edge cases and return the value
for loop for each element start with since 2:
    [0, 1, 2, 3, 4, 5, 6]
           1 +2 +3 +5 + 8
create an array
    f1 = 0
    f2 = 1
iterate for array:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
'''