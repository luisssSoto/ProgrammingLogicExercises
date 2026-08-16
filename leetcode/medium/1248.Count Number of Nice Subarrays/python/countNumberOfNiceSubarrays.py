# 1248. Count Number of Nice Subarrays

def number_of_subarrays(nums: list[int], k: int) -> int:
    from collections import defaultdict
    counts = defaultdict(int)
    counts[0] = 1
    curr = ans = 0
    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1
    return ans

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcase
nums1 = [2,2,2,1,2,2,1,2,2,2,7]
k1 = 2
print(number_of_subarrays(nums1, k1))