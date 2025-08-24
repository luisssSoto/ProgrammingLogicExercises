"""Single Number"""
# Approach 1.
def single_number(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        for i in range(len(nums)):
            if nums[i] not in nums[i + 1: ] and nums[i] not in nums[:i]:
                return nums[i]

data1 = [4,1,2,1,2]
print(single_number(data1))
'''test'''
def test_single_number():
    assert single_number(data1) == 1

'''Complexity Analysis:
Time Complexity: O(N2)
Space Complexity: O(1)'''

# Approach 2.
def single_number(nums):
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        tortoise = 0
        hare = 1
        for _ in range(len(nums) // 2):
            if nums[tortoise] != nums[hare]:
                return nums[tortoise]
            tortoise += 2
            hare += 2
        return nums[hare - 1]

'''Complexity Analysis:
Time Complexity: O(N log N)
Space Complexity: O(1)'''

'''Best solution by anonymous'''
def singleNumber(nums):
        ans=0
        for i in nums:
            ans=ans^i
            # 110
            # 010
            # 100
            print(bin(ans))
        return ans

print(singleNumber(data1))
