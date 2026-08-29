"""49. Group Anagrams"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    ans = []
    for key in anagrams:
        ans.append(anagrams[key])
    return ans

'''Complexity Analysis:
Time Complexity: O(N * Klogk): where N is the length of strs, and 
K is the maximum length of a string in strs. The outer loop has complexity 
O(N) as we iterate through each string. Then, we sort each string in O(KlogK) 
time.
Space Complexity: O(N * K)'''