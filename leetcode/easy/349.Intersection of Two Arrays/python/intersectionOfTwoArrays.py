"""Intersection of Two Arrays"""

def intersection(nums1, nums2):
        unique_elements = []
        for num in nums1:
            if num in nums2 and num not in unique_elements:
                unique_elements.append(num)
        return unique_elements

'''Complexity Analysis:
Time Complexity: O(N * M)
Space Complexity: O(N)'''