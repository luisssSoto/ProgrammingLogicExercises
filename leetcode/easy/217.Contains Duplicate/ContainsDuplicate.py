"""217. Contains Duplicate"""

'''1. approach'''
def contains_duplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

test1 = [1,2,3,4]
print(contains_duplicate(test1))

def test_contains_duplicate():
    assert contains_duplicate(test1) == True

'''2. hash set approach'''
def contains_duplicate(nums):
    s = set()
    for element in nums:
        if element in s:
            return True
        s.add(element)
    return False

print(contains_duplicate(test1))
def test_contains_duplicate():
    assert contains_duplicate(test1) == True
'''
1.
input: integer array
output: boolean as a result of the condition if the element is twice or more will be
true else will be false

2. 
iterate the array
count of elements 
two for loop i and j range
conditional statement if the count >= 2: then break and return False
else: return True

3.
This approah exceeds the time complexity
for i in range of length nums - 1
    for j in range of length nums -1 but start from i + 1
        if i element == j:
            then return False
    return True
    
4. 
[0,1,2,3]
'''