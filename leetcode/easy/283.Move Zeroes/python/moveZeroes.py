"""Move Zeroes"""
'''two pointer technique'''
def move_zeroes(nums):
    write_pointer = 0
    for read_pointer in range(len(nums)):
        if nums[read_pointer] != 0:
            nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            write_pointer += 1
    return nums

data1 = [0,1,0,3,12]
print(move_zeroes(data1))
