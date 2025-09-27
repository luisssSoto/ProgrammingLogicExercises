"""Missing Ranges"""

def missing_ranges(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    if len(nums) == 0:
        return [[lower, upper]]
    matrix = []
    index = 0
    while lower < upper:
        if lower < nums[index]:
            section = [lower, nums[index] -1]
            matrix.append(section)
            lower = nums[index] + 1
        else:
            lower += 1
        index += 1
        if index == len(nums) and nums[-1] < upper:
            section = [lower, upper]
            matrix.append(section)
            lower = upper
    return matrix

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''