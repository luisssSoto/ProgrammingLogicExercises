#  class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

# Approach 1: Hash Table Map two pass
def twoSum(nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                indexes = []
                indexes.append(nums_dict[nums[i]])
                indexes.append(i)
                nums_dict[nums[i]] = indexes
            else:
                nums_dict[nums[i]] = i
        print(f"nums dict:{nums_dict}")
        matches = []
        for num in nums:
            matches.append(nums_dict[num])
            difference = target - num
            if difference in nums_dict and nums_dict[difference] not in matches :
                print(f"difference dict: {nums_dict[difference]}")
                matches.append(nums_dict[difference])
                return matches
            else:
                matches = []
        return nums_dict[target // 2]

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''


def twoSum(nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''