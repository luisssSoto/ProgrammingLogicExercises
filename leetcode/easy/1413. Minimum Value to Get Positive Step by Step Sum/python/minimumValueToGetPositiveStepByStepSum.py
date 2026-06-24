#1413. Minimum Value to Get Positive Step by Step Sum

def min_start_value(nums: list[int]) -> int:
    minimum = nums[0]
    prefix_sum = nums[0]
    for i in range(1, len(nums)):
        prefix_sum += nums[i]
        minimum = min(prefix_sum, minimum)
    if minimum < 0:
        return abs(minimum) + 1
    else:
        return 1

    
# Testcases
nums1 = [-3,2,-3,4,2]
nums2 = [2,3,5,-5,-1]
print(min_start_value(nums2))
print(-2 + 1)