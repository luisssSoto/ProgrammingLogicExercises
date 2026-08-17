# Sherlock and Array

def balanced_sums(arr: list[int]) -> str:
    total = sum(arr)
    left_sum = 0
    for num in arr:
        right_sum = total - left_sum - num
        if right_sum == left_sum:
            return 'YES'
        left_sum += num
    return 'NO'

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''