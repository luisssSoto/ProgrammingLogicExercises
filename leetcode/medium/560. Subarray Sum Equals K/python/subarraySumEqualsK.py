# 560. Subarray Sum Equals K

def subarraySum(nums: list[int], k: int) -> int:
    from collections import defaultdict
    count_vals = defaultdict(int)
    curr = count = 0
    count_vals[0] += 1
    for num in nums:
        curr += num
        missing_val = curr - k
        if missing_val in count_vals:
            count += count_vals[missing_val]
        count_vals[curr] += 1
    return count


'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''