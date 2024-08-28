"""448.Find All Numbers Dissapeared in an Array"""

def find_all_numbers_disappeared(nums):
    nums.sort()
    disappeared_nums = []
    length = len(nums) + 1
    step = 0 
    for i in range(step, len(nums) + 1):
        if nums[i] != i + 1:
            step += 1
    
        
            
data1 = [4,3,2,7,8,2,3,1]
data2 = [1,1]
data3 = [2,2]
print(find_all_numbers_disappeared(data1))

'''
1.
input: int array
output: int array of all the numbers are disappeared in the first array

2.
conditional statement if max number equal length nums
    then complete the numbers between them
else 
    then complete the numbers above it
    

3. 
sort nums
if length of nums == max(nums)
    for i in range(steplen(nus)-1):
        if nums[i] == nums[i+1]:
            del nums[i]
            count_del += 1
    new_list = x for x in range(1,len(nums)+1)
    for number in new_list:
        if number not in nums
            number.append(number)
    return nums[len(nums)-count_del:]
else
    for i in range(steplen(nus)-1):
        if nums[i] == nums[i+1]:
            count_del += 1
    new_list = x for x in range(1,len(nums)+1)
    for number in new_list:
        if number not in nums:
            nums.append(number)
    return nums[len(nums)-count_del:]
    
    
4.
happy coding implement sort burble method in order to sort the nums arr

    
'''