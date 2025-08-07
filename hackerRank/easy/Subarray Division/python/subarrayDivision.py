"""Subarray Division"""

def birthday(s, d, m):
    matches = 0
    if len(s) == m and sum(s) == d:
        return 1
    for i in range(len(s) - m + 1):
        result = 0
        for j in range(m):
            result += s[i + j]
        if result == d:
            matches += 1
    return matches

'''Complexity Analysis:
Time Complexity: O(N + M)
Space Complexity: O(1)'''