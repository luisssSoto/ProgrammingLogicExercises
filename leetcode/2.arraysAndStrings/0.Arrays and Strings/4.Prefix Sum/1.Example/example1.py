def answer_queries(nums: list[int], queries: list[list[int]], limit: int) -> list[int]:
    prefix_sum = [nums[0]]
    ans = []
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[len(prefix_sum)-1])
    for i in range(len(queries)):
        right_bound = prefix_sum[queries[i][1]]
        left_bound = 0
        if queries[i][0] > 0:
            left_bound = prefix_sum[queries[i][0] - 1 ]
        res = right_bound - left_bound
        if res < limit:
            ans.append(True)
        else:
            ans.append(False)
    return ans

# Testcase
nums1 = [1, 6, 3, 2, 7, 2]
queries1 = [[0, 3], [2, 5], [2, 4]]
limit1 = 13

print(answer_queries(nums1, queries1, limit1))


def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        print(x, y, sep="|")
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans

print(answer_queries(nums1, queries1, limit1))