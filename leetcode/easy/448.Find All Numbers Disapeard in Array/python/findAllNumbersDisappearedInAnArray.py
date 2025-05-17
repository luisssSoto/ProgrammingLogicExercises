"""Find All Numbers Disappeared in an Array"""
def find_all_numbers(nums):
    '''find all the numbers that there are not in nums'''
    unique_nums = set(nums)
    missing_nums = []
    for num in nums:
        unique_nums.add(num)
    for i in range(1, len(nums) + 1):
        if i not in unique_nums:
            missing_nums.append(i)
    return missing_nums


# Testing
data_test_0 = [4,3,2,7,8,2,3,1]
data_test_1 = [1,1]
print(find_all_numbers(data_test_0))

