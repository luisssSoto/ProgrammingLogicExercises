"""Remove Element"""
# Approach 1: Two Pointers Technique while
def remove_element(nums, val):
    reader_pointer = 0
    writer_pointer = 0
    while reader_pointer < len(nums):
        if nums[reader_pointer] != val:
            nums[writer_pointer] = nums[reader_pointer]
            writer_pointer += 1
            reader_pointer += 1
        else: 
            reader_pointer += 1
    print(nums)
    return writer_pointer

# Testing
data2 = [0,1,2,2,3,0,4,2]
print(remove_element([1], 1))

# Approach 2: Two Pointers Technique for
def remove_element(nums, val):
    writer_pointer = 0
    for reader_pointer in range(len(nums)):
        if nums[reader_pointer] != val:
            nums[writer_pointer] = nums[reader_pointer]
            writer_pointer += 1
    print(nums)
    return writer_pointer

'''Complexity analysis

Time complexity : O(n).
Assume the array has a total of n elements, both i and j traverse at most 2n steps.

Space complexity : O(1).'''

# Approach 3: Pythonistic solution
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