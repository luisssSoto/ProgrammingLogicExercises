"""Max Consecutive Ones II"""
# Approach 1: Sliding Window
def find_max_consecutive_ones(nums):
    left_pointer = 0
    right_pointer = 0
    longest_sequence = 0
    amount_zeroes = 0
    while right_pointer < len(nums):
        if nums[right_pointer] == 0:
            amount_zeroes += 1
        while amount_zeroes == 2:
            if nums[left_pointer] == 0:
                amount_zeroes -= 1
            left_pointer += 1
        if right_pointer - left_pointer + 1 > longest_sequence:
            longest_sequence = right_pointer - left_pointer + 1
        right_pointer += 1
    return longest_sequence
        
# Testing 
dataTest0 = [1,0,1,1,0]
dataTest1 = [1,0,1,1,0,1]
dataTest3 = [1,0,0,1,1,0,1]
print(find_max_consecutive_ones(dataTest3))

'''Complexity Analysis
Let n be equal to the length of the input nums array.

Time complexity : O(n). Since both the pointers only move forward, 
each of the left and right pointers traverse a maximum of n steps. 
Therefore, the time complexity is O(n).

Space complexity : O(1).
We don't store anything other than variables. 
Thus, the space we use is constant because it is not correlated to 
the length of the input array.'''