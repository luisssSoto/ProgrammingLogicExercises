"""Equal Sides Of An Array"""

def find_even_index(arr):
    left_arr = arr[:0]
    right_arr = arr[1:]
    for i in range(len(arr) - 1):
        if sum(left_arr) == sum(right_arr):
            return i
        left_arr.append(arr[i])
        right_arr.pop(0)
    if sum(left_arr) == sum(right_arr):
            return len(arr) - 1
    return -1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''