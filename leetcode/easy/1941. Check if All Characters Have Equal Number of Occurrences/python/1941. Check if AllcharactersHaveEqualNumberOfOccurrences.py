# 1941. Check if All Characters Have Equal Number of Occurrences

def are_occurrences_equal(s: str) -> bool:
    from collections import defaultdict
    occurrences = defaultdict(int)
    for letter in s:
        occurrences[letter] += 1
    return len(set(occurrences.values())) == 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(k)'''

def are_occurrences_equal(s: str) -> bool:
    from collections import Counter
    return len(set(Counter(s).values())) == 1

# Testcase
s1 = "abacbc"
print(are_occurrences_equal(s1))