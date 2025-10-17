"""Array Partition"""

def arrayPairSum(nums: list[int]) -> int:
        nums.sort()
        print(f"nums: {nums}")
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

'''Complexity Analysis: 
Time Complexity: O(N log N)
Space Complexity: O(N) Timsort using by Python to order the array'''