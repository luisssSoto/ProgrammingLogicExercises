"""Check if the array is sorted"""

def check(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    cnt = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            cnt += 1
    if cnt > 1:
        return False
    else:
        return True
    
"""Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)"""