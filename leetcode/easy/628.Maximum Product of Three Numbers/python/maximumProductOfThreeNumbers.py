def maximum_product(nums: list[int]) -> int:
    nums.sort()
    print(nums)
    product1 = 1
    for num in map(lambda x: x, nums[-3:]):
        product1 *= num
    product2 = nums[0] * nums[1] * nums[-1]
    return max(product1, product2)

'''Complexity Analysis:
Time Complexity: O(N log N)
Space Complexity: O(N)'''