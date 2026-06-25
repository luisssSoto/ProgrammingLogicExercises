# 2090. K Radius Subarray Averages

def radius(nums: list[int], k: int) -> list[int]:
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i - 1])
    left = left_sum = 0
    right = k + k
    length = right + 1
    avgs = [num for num in nums]
    for i in range(len(nums)):
        if i < k:
            avgs[i] = -1
        elif i >= k and right < len(nums):
            avgs[i] = (prefix_sum[right] - left_sum) // length
            right += 1
            left_sum = prefix_sum[left]
            left += 1
        else:
            avgs[i] = -1
    return avgs

# Testcases
nums1 = [7,4,3,9,1,8,5,2,6]
k1 = 3
nums2 = [100000]
k2 = 0
nums3 = [8]
k3 = 100000
print(radius(nums3, k3))

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''