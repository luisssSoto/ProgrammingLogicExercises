"""Longest Harmonious Subsequence"""

def find_LHS(nums: list[int]) -> int:
    frequency = {}
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    longest_sub = 0
    for key in frequency.keys():
        if key + 1 in frequency:
            current_count = frequency[key] + frequency[key + 1]
            if current_count > longest_sub:
                longest_sub = current_count
    return longest_sub

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''