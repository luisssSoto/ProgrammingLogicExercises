"""Divisible Sum Pairs"""

def divisible_sum_pairs(n, k, ar):
    matches = 0
    for i in range(n - 1):
        for j in range(i + 1 , n):
            if (ar[i] + ar[j]) % k == 0:
                matches += 1
    return matches

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''