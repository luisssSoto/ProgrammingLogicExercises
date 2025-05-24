"""Minimum Size Subarray Sum"""

def minimum_size(target, nums):
    """Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or 
equal to target. If there is no such subarray, return 0 instead"""
    left_pointer = 0
    sum_of_current_window = 0
    result = float('inf')
    for right_pointer in range(len(nums)):
        sum_of_current_window += nums[right_pointer]
        while sum_of_current_window >= target:
            result = min(result, right_pointer - left_pointer + 1)
            sum_of_current_window -= nums[left_pointer]
            left_pointer += 1
    return result if result != float('inf') else 0 
# Testing 
target = 7
nums = [2,3,1,2,4,3]
target = 4
nums = [1,4,4]
target = 11
nums = [1,1,1,1,1,1,1,1]
target = 15
nums = [1,2,3,4,5]
target = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
print(minimum_size(target, nums))

'''Complexity Analysis
Here n is the length of nums.
Time complexity: O(n).

You may be thinking: there is an inner while loop inside 
another for loop, isn't the time complexity O(n 2)? The reason
it is still O(n) is because the right pointer right can move 
n times and the left pointer left can move also n times in 
total. The inner loop is not running n times for each 
iteration of the outer loop. A sliding window guarantees a 
maximum of 2n window iterations. This is what is referred to 
as amortized analysis - even though the worst case for an 
iteration inside the for loop is O(n), it averages out to O(1)
when you consider the entire runtime of the algorithm.

Space complexity: O(1).
We are not using any extra space other than a few integer 
variables:left_pointer, right_pointer, sum_of_current_window, 
and result, which takes up constant space each.'''