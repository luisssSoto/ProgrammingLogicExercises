"""Palindrome Permutation"""

def can_permute_palindrome(s: str) -> bool:
    pairs_chr = {}
    for letter in s:
        if letter not in pairs_chr:
            pairs_chr[letter] = 1
        else:
            pairs_chr[letter] += 1
    count_odd = 0
    for (key, val) in pairs_chr.items():
        if val % 2 != 0:
            count_odd += 1
            if count_odd > 1:
                return False
    return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Approach 2. more pythonistic

def can_permute_palindrome(s: str) -> bool:
    from collections import Counter
    amount_chrs = Counter(s)
    odds = sum(val % 2 for val in amount_chrs.values())
    return odds <= 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''