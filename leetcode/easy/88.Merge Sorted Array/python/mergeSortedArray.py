"""Merge Sorted Array"""
# Approaching 1: Merge and sort
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

'''Time complexity: O((n+m)log(n+m)).

The cost of sorting a list of length x using a built-in sorting algorithm is O(xlogx). 
Because in this case, we're sorting a list of length m+n, we get a total time complexity 
of O((n+m)log(n+m)).

Space complexity: O(n), but it can vary.

Most programming languages have a built-in sorting algorithm that uses 
O(n) space.'''

# Approach 2: Three pointers technique
def merge(nums1, m, nums2, n):
    pointer1 = m - 1
    pointer2 = n - 1
    for pointer3 in range(m + n - 1, -1, -1):
        if pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
            elif nums1[pointer1] <= nums2[pointer2]:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
        elif pointer1 >= 0:
            nums1[pointer3] = nums1[pointer1]
            pointer1 -= 1
        else:
            nums1[pointer3] = nums2[pointer2]
            pointer2 -= 1
    return nums1

# Testing
nums1 = [1]
m = 1
nums2 = [0] 
n = 0

print(merge(nums1, m, nums2, n))

'''Complexity Analysis

Time complexity: O(n+m).

Same as Approach 2.

Space complexity: O(1).

Unlike Approach 2, we're not using an extra array.'''