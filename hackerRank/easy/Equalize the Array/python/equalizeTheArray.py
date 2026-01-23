"""Equalize The Array"""

def equalize_array(arr: list[int]) -> int:
    frequency = {}
    max_val = 1
    for ele in arr:
        frequency[ele] = frequency.get(ele, 0) + 1
        max_val = max(frequency[ele], max_val)
    return len(arr) - max_val

def equalize_array(arr: list[int]) -> int:
    from collections import Counter
    frequency = Counter(arr)
    return len(arr) - max(frequency.values())