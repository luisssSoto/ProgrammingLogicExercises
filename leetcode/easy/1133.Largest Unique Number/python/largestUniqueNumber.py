# 1133.Largest Unique Number

def largest_unique_number(nums: list[int]) -> int:
    from collections import defaultdict
    count_freq = defaultdict(int)
    for num in nums:
        count_freq[num] += 1
    largest = -1
    for key, val in count_freq.items():
        if val == 1 and key > largest:
            largest = key
    return largest

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''