"""Climbing Stairs"""

# Approach 4: Fibonacci Number
def climbing_stairs(n):
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second

# Testing
n0 = 2
n1 = 3
print(climbing_stairs(7))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''