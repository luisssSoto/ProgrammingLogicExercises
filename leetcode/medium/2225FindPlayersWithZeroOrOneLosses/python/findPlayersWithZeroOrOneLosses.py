# 2225. Find Players With Zero Or One Losses 

def find_winners(matches: list[list[int]]) -> list[list[int]]:
    count_vals = {}
    for nums in matches:
        if nums[0] not in count_vals:
            count_vals[nums[0]] = 0
        if nums[1] not in count_vals:
            count_vals[nums[1]] = 1
        elif nums[1] in count_vals:
            count_vals[nums[1]] += 1
    non_losses = []
    one_lose = []
    for key in count_vals:
        if count_vals[key] == 0:
            non_losses.append(key)
        elif count_vals[key] == 1:
            one_lose.append(key)
    non_losses.sort()
    one_lose.sort()
    ans = [non_losses, one_lose]
    return ans

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''
