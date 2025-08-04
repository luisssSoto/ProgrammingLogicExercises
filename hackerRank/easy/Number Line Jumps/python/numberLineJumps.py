"""Number Line Jumps"""

def kangaroo(x1, v1, x2, v2):
    result = "no"
    for i in range(10_000):
        if x1 == x2:
            result = "yes"
            break
        x1 += v1
        x2 += v2
    return result.upper()

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''