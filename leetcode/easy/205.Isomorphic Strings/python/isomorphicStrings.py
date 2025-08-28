"""Isomorphic Strings"""

# Approach 1: One Dict
def is_isomorphic(s, t):
    iso_dict = {}
    for i in range(len(s)):
        if s[i] in iso_dict and t[i] != iso_dict[s[i]]:
            return False
        elif s[i] not in iso_dict and t[i] in iso_dict.values():
            return False
        iso_dict[s[i]] = t[i]
    return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Approach 2: Two Dict
def is_isomorphic(s: str, t: str) -> bool:
    mapping_s_t = {}
    mapping_t_s = {}
    for c1, c2 in zip(s, t):
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
    return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

print(is_isomorphic("badc", "baba"))