"""Majority Element"""

# Approach 1:
def majority_element(nums: List[int]) -> int:
    nums_dict = {}
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1
    max_val = float("-inf")
    result = 0
    for key, val in nums_dict.items():
        if val > max_val:
            max_val = val
            result = key
    return result

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Approach 2:
def majority_element(nums: List[int]) -> int:
    nums.sort()
    max_times = 0
    times = 0
    result = 0
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            times += 1
        if nums[i] != nums[i + 1] or i == len(nums) - 2:
            if times > max_times:
                max_times = times
                result = nums[i]
            times = 0
    return result

'''Complexity Analysis:
Time Complexity: O(NlogN)
Space Complexity: O(1)'''

# Approach 3: Boyer-Moore
def majority_element(nums: List[int]) -> int:
    candidate = nums[0]
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''