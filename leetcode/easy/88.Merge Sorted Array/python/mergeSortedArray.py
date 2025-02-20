"""Merge Sorted Array"""
def merge(nums1, m, nums2, n):
    if n == 0:
        return nums1
    else:
        nums2_index = 0
        for i in range(m, len(nums1), 1):
            nums1[i] = nums2[nums2_index]
            nums2_index+=1
    # burble sort approach, alternatively use sort() method (it is faster)
    is_it_sorted = False
    while is_it_sorted == False:
        is_it_sorted = True
        for i in range(len(nums1) - 1):
            if nums1[i] > nums1[i + 1]:
                is_it_sorted = False
                nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
merge(nums1, m, nums2, n)

#1. input: two arrays and two integers
#   output: one array of integers as a result of the merge two arrays according
#   to the amount of elements in m and n parameters

#2. Doing a lists according the m and n variables
#   Merged them into a nums1
#   Sort the nums1 list

#3. conditional statement if m < 1 then create an empty list
#   else then
#   nums1 = nums1 with a length m
#   conditional statement if n < 1 then create an empty list
#   else then
#   nums2 = nums2 with a length n
#   nums1 += nums2
#   nums1 use sort method and it's all

#4. new plan
#   delete the elements in-place