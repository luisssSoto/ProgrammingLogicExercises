"""49. Group Anagrams"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = "".join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

'''Complexity Analysis:
Time Complexity: O(N * K log k): where N is the length of strs, and 
K is the maximum length of a string in strs. The outer loop has complexity 
O(N) as we iterate through each string. Then, we sort each string in O(KlogK) 
time.
Space Complexity: O(N * K)'''