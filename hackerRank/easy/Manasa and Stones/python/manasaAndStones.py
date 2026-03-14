"""Manasa and Stones"""

def stones(n, a, b):
    # Write your code here
    results = set()
    for i in range(n):
        value = (n - 1 - i) * a + i * b
        results.add(value)
    return sorted(results)

'''Complexity Analysis:
Time Complexity: O(N log N)
Space Complexity: O(N)'''