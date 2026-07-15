# 1456. Maximum Number of Vowels in a Substring of Given Length

def max_vowels(s: str, k: int) -> int:
    def is_vowel(ch):
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            return True
        else:
            return False
    left = 0 
    initial_win = []
    count_vowels = 0
    for i in range(k):
        if is_vowel(s[i]):
            count_vowels += 1
        initial_win.append(s[i])
    max_count = count_vowels
    for right in range(k, len(s)):
        if is_vowel(initial_win[left]):
            count_vowels -= 1
        left += 1
        initial_win.append(s[right])
        if is_vowel(initial_win[right]):
            count_vowels += 1
        max_count = max(max_count, count_vowels)
    return max_count

# Testcase
s1 = "abciiidef"
k1 = 3
print(max_vowels(s1,k1))

a = ["a","b","c"]


