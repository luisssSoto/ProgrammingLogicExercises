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
l = []