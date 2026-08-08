# 2248. Intersection of Multiple Arrays

def intersection(nums: list[list[int]]) -> list[int]:
    hash_map = {x:0 for x in range(1, 1001)}
    intersection_vals = []
    length_nums = len(nums)
    for array in nums:
        for val in array:
            if val in hash_map:
                hash_map[val] += 1
    for key, val in hash_map.items():
        if val == length_nums:
            intersection_vals.append(key)
    print(f"hash map: {hash_map}")
    print(f"intersection vals: {intersection_vals}")
    return intersection_vals

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcase
nums1 = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(intersection(nums1))