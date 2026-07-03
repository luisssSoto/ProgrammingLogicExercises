# 2540. Minimum Common Value
def minimum_common_value(nums1: list[int], nums2: list[int]) -> int:
    left = right = 0
    while nums1[left] != nums2[right]:
        while nums1[left] < nums2[right]:
            left += 1
            if left > len(nums1)-1:
                return -1
        while nums1[left] > nums2[right]:
            right += 1
            if right > len(nums2)-1:
                return -1
    return nums1[left]

# Testcase
nums2 = [1,2,3,6]
nums1 = [2,3,4,5]
print(minimum_common_value(nums1, nums2))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''