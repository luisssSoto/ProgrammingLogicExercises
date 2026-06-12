# Example 4: Given an integer array nums and an integer k, find the sum of the subarray 
# with the largest sum whose length is k.

def fixed_window_size(nums: list[int], k: int) -> int:
    curr = 0
    for i in range(k):
        curr += nums[i]
    ans = curr
    for i in range(k, len(nums)):
        print(nums[i])
        print(nums[k])
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    return ans

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''

# Testcase
nums = [3, -1, 4, 12, -8, 5, 6]
k = 4
print(fixed_window_size(nums, k))