"""The Generator Hashtag"""

def generator_hashtag(s):
    if len(s) == 0:
        return False
    s = s.strip()
    s = s.title()
    s = s.split()
    s = ''.join(s)
    s = "#" + s
    if len(s) > 140 or len(s) == 0:
        return False
    return s

# Testing
s0 = " Hello there thanks for trying my Kata"
s1 = "    Hello     World   "
s2 = ""
print(generator_hashtag(s0))

'''Complexity Analysis:
Time Complexity: O(N) where N is the length of the array
Space Complexity: O(1)
'''
t = "ehe leke eltjl"
print(t.title())