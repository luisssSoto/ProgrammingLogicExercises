"""Next Greater Element I"""

def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    hashmap = {}
    for num in nums2:
        while stack and num > stack[-1]:
            hashmap[stack.pop()] = num
        stack.append(num)
    return [hashmap.get(num, -1) for num in nums1]

n1 = [4,1,2]
n2 = [1,3,4,2]
print(next_greater_element(n1, n2))