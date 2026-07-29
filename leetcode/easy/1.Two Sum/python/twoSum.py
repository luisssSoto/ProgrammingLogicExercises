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
        matches = []
        for num in nums:
            matches.append(nums_dict[num])
            difference = target - num
            if difference in nums_dict and nums_dict[difference] not in matches :    
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

# Brute Force:
def two_sum(nums: list[int], target: int) -> list[int]:
     for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

'''Complexity Analysis:
Time Complexity: O(N2)
Space Complexity: O(1)'''
                
# Hash Table: one pass
def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i, val in enumerate(nums):
        missing_val = target - val
        if missing_val in hash_map:
            return [hash_map[missing_val], i]
        elif nums[i] not in hash_map:
            hash_map[val] = i

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''