"""Max Consecutive Ones"""

def longest_ones(nums: list[int], k: int) -> int:
    left = ans = curr = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''

# Testcase
nums1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2
print(longest_ones(nums1, k1))

nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3
print(longest_ones(nums2, k2))