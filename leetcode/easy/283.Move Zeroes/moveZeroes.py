"""Move Zeroes"""
def move_zeroes(nums):
    if len(nums) <= 1:
        return nums
    else:
        zeroes = 0
        for number in nums:
            if number == 0:
                zeroes += 1
        times = 0
        while times <= zeroes:
            for i in range(len(nums)-1):
                if nums[i] == 0:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            times += 1
    return nums

data1 = [0,0,0,3,0]
print(move_zeroes(data1))
'''
1.
input: integer array
output: integer array which all the zeroes are at the end of it

2.
edge: cases: length of the array < 1 return the same
iterate the array
conditional statement ask if the element is 0
if so move it at the end

3. 
if len(nums) <= 1 then return nums
else
    for i in range(nums):
    if i == 0 then zeroes +=1
    zeroes = 0
    while times <= zeroes
    for i in range(len(nums)-1):
        if nums[i] == 0:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    time += 1
        

4. could work but It could be better
'''

'''better approach'''
def moveZeroes4(nums):
    lastNonZeroIdx = 0
    N = len(nums)
    for i in range(N):
        if nums[i] != 0:
            if i != lastNonZeroIdx:
                # swap
                nums[i], nums[lastNonZeroIdx] = nums[lastNonZeroIdx], nums[i]
            lastNonZeroIdx += 1
    return nums

data1 = [0,1,0,3,12]
print(moveZeroes4(data1))