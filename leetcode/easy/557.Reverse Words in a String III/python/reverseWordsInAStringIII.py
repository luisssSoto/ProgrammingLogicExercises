"""Reverse Words in a String III"""

def reverse_words(s):
    """Given a string s, reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial 
word order."""
    s_list = s.split()
    reversed_obj = reversed(s)
    i = 0
    word = ""
    reverse_count = len(s_list) - 1
    for character in reversed_obj:
        i += 1
        if character == " ":
            s_list[reverse_count] = word
            word = ""
            reverse_count -= 1
        else:
            word += character
            if i == len(s):
                s_list[reverse_count] = word
    s = " ".join(s_list)
    return s

# Testing
s = "Let's take LeetCode contest"
print(reverse_words(s))


# Approach 1: Two Pointers Technique
def reverse_words(s):
    s_list = [x for x in s]
    left_pointer = 0
    right_pointer = 0
    last_space = 0
    while right_pointer < len(s):
        if s_list[right_pointer] == " " or right_pointer == len(s) - 1:
            last_space = right_pointer
            if right_pointer == len(s) - 1:
                right_pointer += 1
            for i in range((right_pointer - left_pointer) // 2):
                s_list[left_pointer], s_list[right_pointer - 1] = s_list[right_pointer - 1], s_list[left_pointer]
                left_pointer += 1
                right_pointer -= 1
            right_pointer = last_space
            left_pointer = right_pointer + 1
        right_pointer += 1
    return "".join(s_list)

s = "Let's take LeetCode contest"
s1 = "Hi world"
print(reverse_words(s))

'''Complexity Analysis
Let N be the length of string s.
Time Complexity: O(N) The outer loop iterates over N characters to find 
the start and end index of every word. The algorithm to reverse the word 
also iterates N times to perform N/2 swaps. Thus, the time complexity is 
O(N+N)=O(N).

Space Complexity: O(1) We use constant extra space to track the last 
space index. You could also argue that we are using O(n) space to build 
the output string (we normally don't count the output as part of the 
space complexity, but in this case we are temporarily using some space 
to build it).
But in Python we can't assign values to the string because they are
immutable, so that we decided to create another array, so we have 
this O(N) Space Complexity'''