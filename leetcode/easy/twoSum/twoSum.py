#  class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
 
def twoSum(nums, target):
    #1. output: the indice of the element that add them, result the target argument
    #2. 
    #a. iterate through the array
    #b. create two list
    #c starting add the first element until the last one and so on
    #d. if the sum is equalto the target, so keep their index in a list
    #e return that list

    # 1. create two lists (1 a copy of numbers and the other an empty list)
    index_list = []
    result = 0
    # 2 .iterate the first element of the numbers and sum it with the other 
    # elements of the copy list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], '+', nums[j])
    # 3. it will be two bucles r
    # 4 . if the sum of the elements is equal the target append the index of 
            result = nums[i] + nums[j]
            if result == target:
                index_list.append(i)
                index_list.append(j)
                return index_list
    # both elements in the empty list
    # 5. return the empty_list

test1 = [3,2,4]
print(twoSum(test1, 6))



