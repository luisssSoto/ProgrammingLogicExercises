"""643.Maximum Average Subarray I"""

def find_max_average(nums: list[int], k: int) -> float:
    begin_window = 0
    current_sum = sum(nums[begin_window: k])
    greatest_sum = current_sum
    for end_window in range(k, len(nums)):
        current_sum -= nums[begin_window]
        begin_window += 1
        current_sum += nums[end_window]
        greatest_sum = max(greatest_sum, current_sum)
    return greatest_sum / k

def find_max_average(nums: list[int], k: int) -> float:
    left = 0
    right = k
    greatest_sum = sum(nums[left: right])
    curr_sum = greatest_sum
    while right < len(nums):
        curr_sum -= nums[left]
        curr_sum += nums[right]
        if curr_sum > greatest_sum:
            greatest_sum = curr_sum
        left += 1
        right += 1
    return greatest_sum / k


# testcases:
nums1 = [1,12,-5,-6,50,3]
k1 = 4
print(find_max_average(nums1, k1))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def find_max_average(nums: list[int], k: int) -> int:
    ans = 0
    for i in range(k):
        ans += nums[i]
    curr = ans
    for i in range(len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    print(ans)
    return ans/k

# Testcase
nums = [1,12,-5,-6,50,3]
k = 4
print(find_max_average(nums, k))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''