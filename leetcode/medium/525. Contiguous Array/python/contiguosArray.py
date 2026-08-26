# 522. Contiguos Array

def find_max_length(nums: list[int]) -> int:
    zero_count_idx = {0: -1}
    ans = count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1
        if count in zero_count_idx:
            ans = max(ans, i - zero_count_idx[count])
        else:
            zero_count_idx[count] = i
    return ans 

# Testcases
nums1 = [0,1,1,1,1,1,0,0,0]
nums2 = [1,1,1,1,1,1,1,1]
print(find_max_length(nums1))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''