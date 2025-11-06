def find_shortest_sub_array(nums: list[int]) -> int:
    from collections import Counter
    count_nums = Counter(nums)
    degree = max(count_nums.values())
    if degree == 1:
        return 1
    smallest_len = len(nums)
    for (key, val) in count_nums.items():
        if val == degree:
            start_win = 0
            end_win = len(nums) - 1
            while start_win != end_win:
                if nums[start_win] == key and nums[end_win] == key:
                    smallest_len = min(smallest_len, len(nums[start_win: end_win + 1]))
                    break
                if nums[start_win] != key:
                    start_win += 1
                if nums[end_win] != key:
                    end_win -= 1
    return smallest_len

'''Complexity Analysis:
Time Complexity: O(N2)
Space Complexity: O(N)'''

def find_shortest_sub_array(nums: list[int]) -> int:
    left, right, count = {}, {}, {}
    for i, x in enumerate(nums):
        if x not in left:
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1
    ans = len(nums)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)
    return ans

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcase
t1 = [1,2,2,3,1,4,2]
print(find_shortest_sub_array(t1))