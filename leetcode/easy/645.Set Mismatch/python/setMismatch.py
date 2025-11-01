"""Set Mismatch"""

# Approach 1: 
def find_error_nums(nums: list[int]) -> list[int]:
    unique_nums = set()
    right_sum = 0
    wrong_sum = 0
    result = []
    for i in range(len(nums)):
        right_sum += i + 1
        if nums[i] not in unique_nums:
            unique_nums.add(nums[i])
            wrong_sum += nums[i]
        else:
            result.append(nums[i])
    result.append(right_sum - wrong_sum)
    return result

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def find_error_nums(nums: list[int]) -> list[int]:
    unique_nums = {}
    for num in nums:
        if num not in unique_nums:
            unique_nums[num] = 1
        else: 
            unique_nums[num] += 1
    dup = mis = 0
    for i in range(1, len(nums) + 1):
        if i in unique_nums:
            if unique_nums[i] == 2:
                dup = i
        else:
            mis = i
    return [dup, mis]

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''