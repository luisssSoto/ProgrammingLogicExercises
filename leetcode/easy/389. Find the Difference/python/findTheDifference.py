'''Find The Difference'''

# Approach 1:
def find_the_difference(s: str, t: str) -> str:
    from collections import Counter
    s = Counter(s)
    t = Counter(t)
    for key, val in t.items():
        if key not in s:
            return key
        elif t[key] != s[key]:
            return key 

'''Complexity: Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Approach 2:
def find_the_difference(s: str, t: str) -> str:
    s = sorted(s)
    t = sorted(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[-1]

'''Complexity: Analysis:
Time Complexity: O(N log N)
Space Complexity: O(N) in python'''