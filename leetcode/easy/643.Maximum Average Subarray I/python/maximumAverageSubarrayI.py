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

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''