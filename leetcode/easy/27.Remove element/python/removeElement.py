"""Remove Element"""
def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums.append(nums[i])
            del nums[i]
            nums.insert(0, 0)
            count += 1
    for j in range(count):
        del nums[0]
        del nums[-1]
    return len(nums)

n = [0,1,2,2,3,0,4,2]
v = 2
print(removeElement(n, v))

#1. input: nums list, integer value
#   output: nums list with all the elements except the integer value and also its length

#2. iterate the list
#   conditional statement: if nums[i] == val
#   if so... delete it
#   returns the length of the list and the modified list

#3. iterate the list
#   conditional statemtent: if nums[i] == val
#   if so.. del nums[i]
#   return len(nums) and nums

#4. coding

def remove_element(nums, val):
    # edge cases:
    if val not in nums:
        return len(nums)
    # normal cases
    else:
        steps_back = 0
        for i in range(len(nums)):
            if nums[i - steps_back] == val:
                del nums[i - steps_back]
                steps_back += 1
    print(nums)
    return len(nums)
data1 = [3,2,2,3]
data2 = [0,1,2,2,3,0,4,2]
print(remove_element(data2, 2))
'''
1. 
input: integer array, integer number
output: integer as length of the array modified without any value equal to val

2.
edge cases: if the value is not in nums return the nums
key: delete all the matches but at the correct index

3.
if val not in nums: return nums
else
    create a variable in order to keep track the correct index to delete
    for i in range(len(nums)) 
        if nums[i - steps_back] == val then
            del nums[i - steps_back]
            steps_back += 1
return nums

4. coding again but with different approach
'''

'''Correct approach regarding instructions'''
"""Remove Element"""

def remove_element(nums, val):
    if val not in nums:
        return len(nums)
    print(nums)
    step, matches = 0, 0
    for i in range(step, len(nums)):
        if nums[step] == val:
            matches += 1
            for j in range(step, len(nums)-1):
                nums[j] = nums[j+1]
            step -= 1
        step += 1
    nums = nums[:len(nums)-matches]
    print(nums)
    return len(nums)
    
            
data1 = [3,2,2,3]
data2 = [0,1,2,2,3,0,4,2]
print(remove_element(data2, 2))
'''
1.
input: integer array, integer value
output: modified integer array according to all elements equal val don't be in the array

2.
edge cases: conditional statement if val not in nums return it
while condition 
iterate nums for loop
conditional statement if element is equal val
setting the element equal to the last element
return the length of the array - variable describe above

3.
if val not in array: return len(array)
for i in range(len(array)):
    if array[i] == val:
        array[i] = array[length]
    
4.
'''

'''Best approach'''
def remove_elements1(nums, val):
    if val not in nums:
        return len(nums)
    print(id(nums))
    nums[:] = list(filter(lambda x: x != val, nums))
    print(nums[:])
    print(id(nums[:]))
    return len(nums)

data1 = [3,2,2,3]
data2 = [0,1,2,2,3,0,4,2]
print(remove_elements1(data1,3))
