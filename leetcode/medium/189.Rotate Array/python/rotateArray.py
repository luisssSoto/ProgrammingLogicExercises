"""Rotate Array"""

# My Approach
def rotate_array(nums, k):
    """Given an integer array nums, rotate the array to the right by k steps, where k 
    is non-negative."""
    spaces_to_move = k % len(nums)
    if spaces_to_move == 0:
        return nums
    begin_nums = nums[-spaces_to_move : ]
    write_pointer = len(nums) - 1
    for read_pointer in range(len(nums) - spaces_to_move - 1, -1, -1):
        nums[write_pointer] = nums[read_pointer]
        write_pointer -= 1
    for i in range(len(begin_nums)):
        nums[i] = begin_nums[i]
    return nums

# Testing
nums0 = [1,2,3,4,5,6,7]
k0 = 3
nums1 = [-1,-100,3,99]
k1 = 2
nums2 = [1,2,3,4]
k2 = 15
# print(rotate_array(nums2, k2))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''
