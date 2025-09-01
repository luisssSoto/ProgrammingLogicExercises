"""387. First Unique Character in a String"""

def first_uniq_char(s):
    characters_count = {}
    for character in s:
        if character not in characters_count:
            characters_count[character] = 0
        else:
            characters_count[character] += 1
    for i in range(len(s)):
        if characters_count[s[i]] == 0:
            return i
    return -1

'''Complexity Analysis:
Time complexity: O(N) since we go through the string of length N two times.
Space complexity: O(1) because English alphabet contains 26 letters.'''


# Approach 2: Pythonistic solution
def firstUniqChar(s):
    import collections
    count = collections.Counter(s)
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1

s1 = "leetcode"
print(firstUniqChar(s1))