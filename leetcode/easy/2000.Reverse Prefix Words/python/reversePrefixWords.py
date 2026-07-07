# Reverse Prefix word

def reverse_prefix_word(word: str, ch: str) -> str:
    word_array = []
    right = 0
    is_there_a_match = False
    for i in range(len(word)):
        if not is_there_a_match and word[i] == ch:
            right = i
            is_there_a_match = True
        word_array.append(word[i])
    if not is_there_a_match:
        return word
    left = 0
    while left < right:
        word_array[left], word_array[right] = word_array[right], word_array[left]
        right -= 1
        left += 1
    return "".join(word_array)

# Testcase
word = "rzwuktxcjfpamlonbgyieqdvhsoqhpeciglmwunfxdbytkjasvzr"
ch = "r"
print(reverse_prefix_word(word, ch))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''
