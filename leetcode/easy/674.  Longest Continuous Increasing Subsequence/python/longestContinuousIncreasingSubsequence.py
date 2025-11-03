"""674. Longest Continuous Increasing Subsequence"""

def find_length(nums):
    greatest_sub = 0
    current_count = 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            current_count += 1
        else:
            if current_count > greatest_sub:
                greatest_sub = current_count
            current_count = 0
        if current_count > greatest_sub:
            greatest_sub = current_count
    return greatest_sub + 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Testcases
t1 = [7, 8, 9, 1, 2, 3]
print(find_length(t1))