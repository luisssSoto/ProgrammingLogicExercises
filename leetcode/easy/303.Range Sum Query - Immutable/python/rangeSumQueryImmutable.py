"""303.Range Sum Query - Immutable"""

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        result = sum(self.nums[left: right + 1])
        return result
    
'''Complexity Analysis:
Time Complexity: O(N) per query
Space Complexity: O(N) per query'''

class NumArray:

    def __init__(self, nums: list[int]) -> None:
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[i - 1] + nums[i])

    def sum_range(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left - 1] 

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity O(N)'''
