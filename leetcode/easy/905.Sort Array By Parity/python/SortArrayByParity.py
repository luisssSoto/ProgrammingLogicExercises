"""905 Sort Array By Parity"""
def sort_array_by_parity(nums):
    if len(nums) <= 1:
        return nums
    else:
        steps_back = 0
        for i in range(len(nums)):
            if nums[i - steps_back] % 2 != 0:
                nums.append(nums[i - steps_back])
                del nums[i - steps_back]
                steps_back += 1
    return nums

data1 = [1,3,5,0]
data2 = [3,1,2,4]
data3 = [0,1,2]
print(sort_array_by_parity(data1))

'''
1. 
input: integer array
output: integer array sorted where all the even numbers are at the begining and 
then the odd ones

2.
edge cases: length <= 1 return the same array
key: if n % 2 == 0 will be an even number otherwise odd and work only with one of them
if it is odd append it and delete it all the other ones keep them at the same position

3. 
if len(nums) <= 1 return nums
else
    variable to compens steps
        iterate by indexing and start i - steps
            if number % 2 != 0 then
                append number at the end nums
                delete number[i]
                steps += 1

4. index is moving when we work in-place be careful
'''

'''Better approach:
Two pointer technique'''

def sort_array_by_parity(nums):
    writePointer = 0
    for readPointer in range(len(nums)):
        if nums[readPointer] % 2 == 0:
            nums[writePointer], nums[readPointer] = nums[readPointer], nums[writePointer]
            writePointer += 1
    return nums

# Testing
nums = [3,1,2,4]
nums1 = [0]
print(sort_array_by_parity(nums))

# Approach 1: Two Pointers Technique
def sort_array_by_parity(nums):
    write_pointer = 0
    for read_pointer in range(len(nums)):
        if nums[read_pointer] % 2 == 0:
            nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            write_pointer += 1
    return nums

# Testing
nums0 = [3,1,2,4]
nums1 = [0]

print(sort_array_by_parity(nums1))

'''Complexity Analysis:
 * Time complexity: O(N)
 * Space complexity: O(1)'''