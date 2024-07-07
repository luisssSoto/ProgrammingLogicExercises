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
print(runningSumOf1DArray(test2))