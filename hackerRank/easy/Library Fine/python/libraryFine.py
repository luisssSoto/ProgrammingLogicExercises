"""Library Fine"""

def library_fine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    if y1 > y2:
        return (y1 - y2) * 10_000
    elif y1 < y2:
        return 0
    if m1 > m2:
        return (m1 - m2) * 500
    elif m1 < m2:
        return 0
    if d1 > d2:
        return (d1 - d2) * 15
    else:
        return 0

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''