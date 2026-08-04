# Counting Elements

def countElements(arr: list[int]) -> int:
    right_vals = set(arr)
    count = 0
    for num in arr:
        if num + 1 in right_vals:
            count += 1
    return count

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''