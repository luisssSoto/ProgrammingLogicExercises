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
'''
Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)
'''

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
Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)
'''