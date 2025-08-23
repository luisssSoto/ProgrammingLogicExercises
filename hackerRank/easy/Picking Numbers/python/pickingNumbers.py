"""Picking Numbers"""

def picking_numbers(a):
    a.sort()
    matches = hare = 1
    max_match = tortoise =  0
    for _ in range(len(a) - 1):
        if a[tortoise] == a[hare] or a[tortoise] + 1 == a[hare]:
            matches += 1
            if matches > max_match:
                max_match = matches
        else:
            tortoise = hare
            matches = 1
        hare += 1
    return max_match

'''Complexity Analysis:
Time Complexity: O(N log N) because of Python's sort() method
Space Complexity: O(1)'''