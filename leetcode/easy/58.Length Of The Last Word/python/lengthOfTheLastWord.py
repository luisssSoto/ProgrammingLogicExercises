"""Length of the Last Word"""

def length_last_word(s):
    s = s.strip()
    pointer = len(s) - 1
    count = 0
    while pointer != -1 and s[pointer] != " ":
        count += 1
        pointer -= 1
    return count

# Testing
s0 = "Hello World"
print(length_last_word(s0))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''