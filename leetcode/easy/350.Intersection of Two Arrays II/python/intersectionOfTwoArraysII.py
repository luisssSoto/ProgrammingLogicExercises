"""Intersection of Two Arrays II"""
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    intersection_list = []
    index_list = []
    count_index = -1
    for i in range(len(nums1)):
        if nums1[i] not in nums2:
            continue
        if nums1[i] in intersection_list:
            for j in range(index_list[count_index],len(nums2)):
                if nums1[i] == nums2[j]:
                    intersection_list.append(nums1[i])
                    index_list.append(j + 1)
                    count_index += 1
                    break
        else:
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    intersection_list.append(nums1[i])
                    index_list.append(j + 1)
                    count_index += 1
                    break
    return intersection_list
    

nums1 = [1,2,2,1]
nums2 = [2,2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))

'''
1.
input: two integer arrays
output: one integer array that shows all the intersection
between them

2. 
sort the arrays
create two lists: index lists and return list
count_index variable = 0
iterate first array
conditional statement if array[i] not in array2: continue
conditional stament if array[i] in return list then
iterate second array from range(len(index_list[count_index]))
conditional statement if array[i] == array[j] then
append the element in return list
and the j in the index list
count += 1
else then
iterate from the begining
conditional statement if array[i] == array[j]
append the element in return list
and the j in the index list
count += 1

3.
sort(nums1)
sort(nums2)
index_list[]
intersections_list[]
count_index = 0
for i in range(len(nums1)):
    if nums1[i] not in nums2:
        continue
    if nums1[i] in intersection_list:
        for j in range(len(index_list[count_index], nums2)):
            if nums1[i] == nums2[j]:
                intersection_list.append(nums1[i])
                index_list.append(j + 1)
                count_index += 1
    else:
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                intersection_list.append(nums1[i])
                index_list.append(j + 1)
                count_index += 1

    
4. Figuring out intersection sets
'''
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]

'''Best solution'''
from collections import Counter

def intersect(nums1, nums2):
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    intersection = []
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))   
    return intersection

print(intersect(nums1, nums2))
i = []
i.extend([4] * min(2,3))
print(i)
i.extend([5] * 5)
print(i)

# Approach 2: 
def intersect(nums1, nums2):
        import collections
        intersection_values = []
        nums1_dict = collections.Counter(nums1)
        nums2_dict = {}
        for num in nums2:
            if num not in nums2_dict:
                nums2_dict[num] = 1
            else:
                nums2_dict[num] += 1
        for key in nums1_dict:
            if key in nums2_dict:
                for i in range(min(nums1_dict[key], nums2_dict[key])):
                    intersection_values.append(key)
        return intersection_values

'''Complexity Analysis:
Time Complexity: O(M + N)
Space Complexity: O(M + N)'''