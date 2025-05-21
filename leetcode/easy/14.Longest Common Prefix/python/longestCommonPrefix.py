"""Longest Common Prefix"""
# My Approach
def longest_common_prefix(strs):
    """Write a function to find the longest common prefix string amongst 
an array of strings."""
    if len(strs) == 1:
        return strs[0]
    common_prefix = ""
    count_matches = 0
    necessary_matches = len(strs) - 1
    shortest_string = strs[0]
    for i in range(1, len(strs)):
        if len(strs[i]) < len(shortest_string):
            shortest_string = strs[i]
    for i in range(len(shortest_string)):
        for j in range(len(strs) - 1):
            if strs[j][i] == strs[j + 1][i]:
                count_matches += 1
            else:
                return common_prefix
            if count_matches == necessary_matches:
                common_prefix += strs[j][i]
                count_matches = 0
    return common_prefix

# Testing
data_test_0 = ["flower","flow","flight"]
data_test_1 = ["dog","racecar","car"]
data_test_2 = [""]
data_test_3 = ["a"]
data_test_4 = ["ab", "a"]
data_test_5 = ["caa","","a","acb"]

print(longest_common_prefix(data_test_5))

'''Complexity Analysis:
Time Complexity: O(N3)
Space Complexity: O(1)'''

# Approach 1: Horizontal Scanning
def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0 : len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix

# Testing 
print(longest_common_prefix(data_test_0))

'''Complexity Analysis
Time complexity : O(S) , where S is the sum of all characters in all 
strings.
Space complexity : O(1). We only used constant extra space.'''