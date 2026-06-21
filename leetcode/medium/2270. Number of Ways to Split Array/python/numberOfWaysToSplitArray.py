#2270. Number of Ways to Split Array

def ways_to_split_array(nums: list[int]) -> int:
    ans = 0
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])
    for i in range(len(prefix_sum)-1):
        if prefix_sum[i] >= prefix_sum[-1] - prefix_sum[i]:
            ans += 1
    return ans

# Testcase
nums1 = [10,4,-8,7]
#[10,14,6,13]
nums2 = [2,3,1,0]
print(ways_to_split_array(nums1))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def ways_to_split_array(nums: list[int]) -> int:
    ans = 0
    left_sum = 0
    for i in range(0, len(nums)):
        left_sum += nums[i]
    right_sum = 0
    for i in range(len(nums)-1, 0, -1):
        right_sum += nums[i]
        left_sum -= nums[i]
        if left_sum >= right_sum:
            ans += 1
    return ans

# Testcase
nums1 = [10,4,-8,7]
#[10,14,6,13]
nums2 = [2,3,1,0]
print(ways_to_split_array(nums1))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def ways_to_split_array(nums: list[int]) -> int:
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1
    return ans

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''