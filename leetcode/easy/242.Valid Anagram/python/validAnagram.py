"""Valid Anagram"""

def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for char in s:
        if char not in s_dict:
            s_dict[char] = 1
        else:
            s_dict[char] += 1        
    for char in t:
        if char not in t_dict:
            t_dict[char] = 1
        else:
            t_dict[char] += 1
    for key, val in s_dict.items():
        if key not in t_dict or val != t_dict[key]:
            return False
    return True

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''