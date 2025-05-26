"""Reverse Words in a String"""

def reverse_words(s):
    """Return a string of the words in reverse order concatenated by a single space."""
    reverse_array = []
    begin_word = 0
    end_word = 0
    while end_word < len(s):
        word = ""
        while s[end_word] != " " and end_word < len(s):
            end_word += 1
            if end_word == len(s):
                break
        if begin_word < end_word:
            word = s[begin_word : end_word]
            reverse_array.insert(0, word)
            begin_word = end_word
        begin_word += 1
        end_word += 1
    s = " ".join(reverse_array)
    return s

# Testing 
s0 = " the sky is blue "
s1 = "  hello world  "
s2 = "a good   example"
s3 = " asdasd df f"
print(reverse_words(s3))

# Approach 1: Built-in methods
def reverse_words(s):
    s = s.split()
    print(s)
    s = " ".join(reversed(s))
    return s

print(reverse_words(s0))

