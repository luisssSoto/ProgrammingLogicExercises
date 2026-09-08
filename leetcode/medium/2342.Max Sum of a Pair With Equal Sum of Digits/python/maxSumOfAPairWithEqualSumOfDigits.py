# 2342. Max Sum of a Pair With Equal Sum of Digits

def maximumSum(nums: list[int]) -> int:
    from collections import defaultdict
    dig_val = defaultdict(int)
    ans = -1
    def get_key(n):
        key = 0
        while n > 0:
                remainder = n % 10
                key += remainder
                n //= 10
        return key
    for num in nums:
        key = get_key(num)
        if key in dig_val:
               ans = max(ans, num + dig_val[key])
        dig_val[key] = max(dig_val[key], num)
    return ans

'''Complexity Analysis:
Time Complexity: O(N log M)
Space Complexity: O(N)'''