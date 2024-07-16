#  class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
 
def twoSum(nums, target):
    index_list = []
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], '+', nums[j])
            result = nums[i] + nums[j]
            if result == target:
                index_list.append(i)
                index_list.append(j)
                return index_list

test1 = [3,2,4]
print(twoSum(test1, 6))



