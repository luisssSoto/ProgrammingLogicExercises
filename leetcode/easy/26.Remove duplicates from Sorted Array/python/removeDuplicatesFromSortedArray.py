"""Remove Duplicated from Sorted Array"""
#Exceeds the time limit
def remove_duplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    step = match = 0
    for i in range(step, len(nums)-1):
        if nums[step] == nums[step+1]:
            match += 1
            for j in range(step, len(nums)-1):
                nums[j] = nums[j+1]
            step -= 1
        step += 1
    print(f'nums: {nums}')
    nums = nums[:len(nums)-match]
    print(f'nums: {nums}')
    return len(nums)

data1 = [0,0,1,1,1,2,2,3,3,4]
data2 = [1,1,2]
data3 = [1,2]
data4 = [1,2,3]
print(remove_duplicates(data1))

'''
1.
input: sorted array of nums
output sorted array but with unique elements in it

2.
iterate array length -1 
conditional statement if i != i+1
if so... array[step] == i+1

3.
match = 0
step = 1
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        nums[step] = nums[i+1]
        step += 1
    else:
        match += 1
nums = nums[:len(nums)-match]
return len(nums)

4.
happy coding!
'''

'''Better approach'''
def remove_duplicates(nums):
    step = 1
    match = 0
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[step] = nums[i+1]
            step += 1
        else:
            match += 1
    nums = nums[:len(nums)-match]
    print(f'modyfied nums: {nums}')
    return len(nums)

data1 = [0,0,1,1,1,2,2,3,3,4]
data2 = [1,1,2]
data3 = [1,2]
data4 = [1,2,3]
print(remove_duplicates(data4))

'''smarter approach and reducess time complexity'''
def removeDuplicates(nums):
        nums[:]=list(sorted(set(nums)))
        print(nums)
        return len(nums)

test0 = [1,1,2]
print(removeDuplicates(test0))

def remove_duplicates(nums):
    writer_pointer = 0
    for reader_pointer in range(len(nums) - 1):
        if nums[reader_pointer] != nums[reader_pointer + 1]:
            writer_pointer += 1
            nums[writer_pointer] = nums[reader_pointer + 1]
    print(nums)
    return writer_pointer + 1

data1 = [0,0,1,1,1,2,2,3,3,4]
data2 = [1,1,2]
data3 = [1,2]
data4 = [1,2,3]
test0 = [1,1,2]
print(remove_duplicates(data4))