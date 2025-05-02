"""Max Consecutive Ones"""
def find_max_consecutive_ones(nums):
    count = 0
    max_consecutive_ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_consecutive_ones = max(max_consecutive_ones, count)
            count = 0
    return max(max_consecutive_ones, count)

# Testing
test1 = [1]
print(find_max_consecutive_ones(test1))


'''
Complexity Analysis:
Time complexity: O(N) Where N is the number of elements in the array
Space complexity: O(1) We do not use any extra space
'''