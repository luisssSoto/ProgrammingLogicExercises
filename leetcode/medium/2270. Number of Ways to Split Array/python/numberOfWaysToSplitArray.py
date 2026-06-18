#2270. Number of Ways to Split Array

def ways_to_split_array(nums: list[int]) -> int:
    ans = 0
    left_sum = [nums[0]]
    for i in range(1, len(nums)-1):
        left_sum.append(left_sum[-1] + nums[i])
    right_sum = [nums[-1]]
    for i in range(len(nums)-2, 0, -1):
        right_sum.append(right_sum[-1] + nums[i])
    for i in range(len(left_sum)):
        if left_sum[i] >= right_sum[len(right_sum) - i - 1]:
            ans += 1
    return ans

# Testcase
nums1 = [10,4,-8,7]
print(ways_to_split_array(nums1))


'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''
