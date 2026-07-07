"""Move Zeroes"""
'''two pointer technique'''
# Move the non zeroes elements not the zeroes
def move_zeroes(nums: list[int]) -> list[int]:
    right = 0
    for left in range(len(nums)):
        if nums[left] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
    return nums

data1 = [0,1,0,3,12]
print(move_zeroes(data1))

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''

def move_zeroes(nums: list[int]) -> list[int]:
    right = 0
    for left in range(len(nums) - 1):
        if nums[left] == 0:
            while right < len(nums) - 1 and nums[right] == 0:
                right += 1
            nums[left], nums[right] = nums[right], nums[left]
        else:
            right += 1
    return nums

'''Complexity Analysis: 
Time Complexity: O(N2)
Space Complexity: O(1)'''