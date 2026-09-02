# 2342. Max Sum of a Pair With Equal Sum of Digits

def maximumSum(nums: list[int]) -> int:
    dig_val = {}
    ans = -1
    for num in nums:
        number = num
        key = 0
        while number > 0:
                remainder = number % 10
                key += remainder
                number //= 10
        if key not in dig_val:
                dig_val[key] = num
        else:
                res = num + dig_val[key]
                if res > ans:
                        ans = res
                if num > dig_val[key]:
                        dig_val[key] = num
    return ans

'''Complexity Analysis:
Time Complexity: O(N log M)
Space Complexity: O(N)'''