"""Array - DS"""

def reverse_array(a):
    last_pointer = len(a) - 1
    for first_pointer in range(len(a) // 2):
        a[first_pointer], a[last_pointer] = a[last_pointer], a[first_pointer]
        last_pointer -=1
    return a

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''