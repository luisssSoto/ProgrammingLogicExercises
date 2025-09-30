"""Missing Number"""

def missing_number(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(nums)

'''Complexity Analysis:
Time Complexity: O(N log N)
Space Complexity: O(1)'''

def missing_number(nums: list[int]) -> int:
    s = set(nums)
    for i in range(len(nums) + 1):
        if i not in s:
            return i
        
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

def missing_number(nums: list[int]) -> int:
    expected_sum = len(nums) * (len(nums) + 1) // 2
    real_sum = sum(nums)
    return expected_sum - real_sum

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''