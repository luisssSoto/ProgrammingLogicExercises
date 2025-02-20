"""Merge Sorted Array"""
def merge_sorted_array(nums1, m, nums2, n):
    for i in range(len(nums1)-1, m-1, -1):
        del nums1[i]
    for j in range(len(nums2)-1, n-1, -1):
        del nums2[j]
    nums1 += nums2
    nums1.sort()
    return nums1

nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge_sorted_array(nums1, m, nums2, n))

'''
1.
input: two integer arrays and two integers
output: first modified array but merged second one and sorted
        non-decreasing order, also according with the integers

2.
edge cases: if m or n is zero return the other array
iterate the first array according its parameter integer
delete elements right side
repeat last operation in second array
merge first array to the second one
sorting whit burble method
return array

3. 
for loop in the range of length -1 starting from here to -1
    delete each element
repeat last instructions
merge the first array to the second one
sorting array with burble method
return array

4.happy coding!
'''