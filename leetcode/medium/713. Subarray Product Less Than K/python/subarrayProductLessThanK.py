"""713. Subarray Product Less Than K"""

def num_subarray_less_than_k(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0
    left = ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1
    return ans

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''

# Testcase
nums = [10,5,2,6]
k = 100
print(num_subarray_less_than_k(nums, k))