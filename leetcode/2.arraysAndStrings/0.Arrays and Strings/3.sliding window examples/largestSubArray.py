#Find the longest subarray with a sum less than or equal to k (constraint metric = sum)
def find_length(nums: list[int], k: int) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)

#Testcase
nums1 = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k1 = 8
print(find_length(nums1, k1))

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''
