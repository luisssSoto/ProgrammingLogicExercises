"""Merge Sorted Array"""
def merge(nums1, m, nums2, n):
    for i in range(len(nums1)):
        if i >= m:
            del nums1[-1]
    for j in range(len(nums2)):
        if j >= n:
            del nums2[-1]
    nums1 += nums2
    nums1.sort()
    print(nums1)
    print(nums2)
    
nums1 = [0]
m = 0
nums2 = [1] 
n = 1
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

import random
random.seed()

random_list = []
print(random.randint(0, 10))