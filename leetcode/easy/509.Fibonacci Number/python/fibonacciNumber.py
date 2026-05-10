"""Fibonacci Recursion"""

def fib(n: int) -> int:
    if n < 1:
        return 0
    if n < 3:
        return 1
    return fib(n -1) + fib(n - 2)

# 0 = 0
# 1 = 1
# 2 -> 0 + 1 = 1
# 3 -> 1 + 1 = 2
# 4 -> 2 + 1 = 3
# 5 -> 3 + 2 = 5

print(fib(5))