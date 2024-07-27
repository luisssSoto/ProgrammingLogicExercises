"""Single Number"""
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
'''
1.
input: integer numbers array
output: integer number that appears only once in the array

2.
edge cases: length == 1 return the first element
iterate the array
if that element in the rest of array continue
else: return that value

3.
if length of the array nums == 1:
    return nums[0]
else:
    for i in range(len(nums)-1):
        if nums[i] not in nums[i + 1:]:
            return nums[i]

4. I'm going to exceed the time complexity or space complexity maybe
'''