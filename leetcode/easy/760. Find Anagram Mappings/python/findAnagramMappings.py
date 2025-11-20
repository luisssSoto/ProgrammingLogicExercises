"""Find Anagram Mappings"""

# Approach 1
def anagram_mappings(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    nums2_dict = {}
    for i, ele in enumerate(nums2):
        if ele not in nums2_dict:
            nums2_dict[ele] = i
    for ele in nums1:
        res.append(nums2_dict[ele])
    return res

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''


# Approach 2
def anagram_mappings(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    for i in range(len(nums1)):
        res.append(nums2.index(nums1[i]))
    return res

'''Complexity Analysis:
Time Complexity: O(N ** 2)
Space Complexity: O(N)'''