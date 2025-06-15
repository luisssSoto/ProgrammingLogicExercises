"""Reverse String"""
# Approach 1: Two Pointer Technique
def reverse_string(s):
    start_pointer = 0
    end_pointer = len(s) - 1
    for _ in range(len(s) // 2):
        s[start_pointer], s[end_pointer] = s[end_pointer], s[start_pointer]
        start_pointer += 1
        end_pointer -= 1
    return s
 
 # Testing
s0 = ["h","e","l","l","o"]
s1 = ["H","a","n","n","a","h"]
print(reverse_string(s1))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Approach 2: Recursive and two pointer technique
def reverse_string(s):
    def reverse_string_recursive(s, start_pointer, end_pointer):
        if start_pointer == len(s) // 2:
            return s
        else:
            s[start_pointer], s[end_pointer] = s[end_pointer], s[start_pointer]
            return reverse_string_recursive(s, start_pointer + 1, end_pointer - 1)
    start_pointer = 0
    end_pointer = len(s) - 1
    return reverse_string_recursive(s, start_pointer, end_pointer)
    
s0 = ["h","e","l","l","o"]
print(reverse_string(s0))