"""Save The Prisioner!"""

def saveThePrisoner(n: int, m: int, s: int)-> int:
    return ((s - 1 + m - 1) % n) + 1

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''