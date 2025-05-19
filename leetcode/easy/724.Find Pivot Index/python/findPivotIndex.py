"""Find Pivot Index"""
def find_pivot_index(nums):
    '''Return the leftmost pivot index. If no such index exists, return -1.'''
    nums.append(0)
    left_sum = 0
    right_sum = 0
    for i in range(1,len(nums)):
        right_sum += nums[i]
    for i in range(len(nums) - 1):
        if right_sum == left_sum:
            return i
        else: 
            left_sum += nums[i]
            right_sum -= nums[i + 1]
    return -1

# Testing 
data_test_0 = [1,7,3,6,5,6]
data_test_1 = [1,2,3]
data_test_2 = [2,1,-1]
data_test_3 = [-1,-1,0,1,1,0]
data_test_4 = [4]

print(find_pivot_index(data_test_3))

'''Complexity Analysis:
Time Complexity: O(N2)
Space Complexity: O(1)'''