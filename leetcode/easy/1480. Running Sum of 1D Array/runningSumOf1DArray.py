"""Running Sum of 1D Array"""
def runningSumOf1DArray(nums):
    new_nums = nums[:1]
    amount = 0
    for i in range(len(nums)-1):
        if i == 0:
            amount += nums[i] + nums[i + 1]
        else:
            amount += nums[i + 1]
        new_nums.append(amount)
    return new_nums

test1 = [1,2,3,4]
test2 = [2,3,4,5]
print(runningSumOf1DArray(test1))

'''Best approaches'''
'''1.'''
def runningSumOf1DArray(nums):
    new_nums = nums[:1]
    for i in range(1, len(nums)):
        new_nums.append(nums[i] + new_nums[i - 1])
    return new_nums

print(runningSumOf1DArray(test1))

'''2.'''
def runningSumOf1DArray(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

print(runningSumOf1DArray(test1))