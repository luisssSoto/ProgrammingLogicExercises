"""290. Word Pattern"""

def word_pattern(pattern: str, s: str) -> bool:
    s = s.split()
    if len(pattern) != len(s):
        return False
    pairs = {}
    unique_words = set()
    for i, ch in enumerate(pattern):
        if ch not in pairs:
            if s[i] in unique_words:
                return False
            pairs[ch] = s[i]
            unique_words.add(s[i])
        elif pairs[ch] != s[i]:
            return False
    return True


def word_pattern(pattern: str, s: str) -> bool:
    map_char = {}
    map_words = {}
    s = s.split()
    if len(pattern) != len(s):
        return False
    for ch, word in zip(pattern, s):
        if ch not in map_char:
            if word in map_words:
                return False
            else:
                map_char[ch] = word
                map_words[word] = ch
        else:
            if map_char[ch] != word:
                return False
    return True

'''Complexity Analysis:
Time Complexity: O(N + M)
Space Complexity: O(N)'''