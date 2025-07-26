"""Left Rotation"""
def left_rotation(d, arr):
    spaces_to_move = d % len(arr)
    right_part = arr[ : spaces_to_move]
    left_part = arr[spaces_to_move : ]
    arr = left_part + right_part
    return arr

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(N)'''