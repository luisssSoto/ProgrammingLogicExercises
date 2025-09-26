"""Summary Ranges"""

n = -2147483648
s = str(n)
print(type(s))

def summary_ranges(nums: list[int]) -> list[str]:
    if len(nums) < 1:
        return []
    elif len(nums) == 1:
        return [str(nums[0])]
    ranges = []
    section = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] - 1 == nums[i - 1]:
            section.append(nums[i])
            if i == len(nums) - 1:
                if len(section) > 1:
                    section = str(section[0]) + "->" + str(section[-1])
                else:
                    section = str(section[0])
                ranges.append(section)
        else:
            if len(section) > 1:
                section = str(section[0]) + "->" + str(section[-1])
            else:
                section = str(section[0])
            ranges.append(section)
            section = [nums[i]]
            if i == len(nums) - 1:
                if len(section) > 1:
                    section = str(section[0]) + "->" + str(section[-1])
                else:
                    section = str(section[0])
                ranges.append(section)
    return ranges 

t1 = [0,1,2,4,5,7]
print(summary_ranges(t1))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def summaryRanges(nums: list[int]) -> list[str]:
        ranges = []     
        i = 0 
        
        while i < len(nums): 
            start = nums[i]  
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            if start != nums[i]: 
                ranges.append(str(start) + "->" + str(nums[i]))
            else: 
                ranges.append(str(nums[i]))
            
            i += 1

        return ranges

print(summaryRanges(t1))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''