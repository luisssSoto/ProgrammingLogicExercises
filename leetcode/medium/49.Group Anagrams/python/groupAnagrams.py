"""49. Group Anagrams"""

def groupAnagrams(strs):
        anagrams_dict = {}
        for word in strs:
            sort_word = sorted(word)
            sort_word = "".join(sort_word)
            if sort_word in anagrams_dict:
                anagrams_dict[sort_word].append(word)
            else:
                anagrams_dict[sort_word] = []
                anagrams_dict[sort_word].append(word)
        anagrams_list = []
        for val in anagrams_dict.values():
            anagrams_list.append(val)

'''Complexity Analysis:
Time Complexity: O(N * Klogk): where N is the length of strs, and 
K is the maximum length of a string in strs. The outer loop has complexity 
O(N) as we iterate through each string. Then, we sort each string in O(KlogK) 
time.
Space Complexity: O(N * K)'''