"""303.Range Sum Query - Immutable"""

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        result = sum(self.nums[left: right + 1])
        return result
    
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''