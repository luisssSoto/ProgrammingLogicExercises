"""Jumping On The Cloud: Revisited"""

def jumping_on_clouds(c: list[int], k:int) -> int:
    count = 0
    index = k % len(c)
    def cumulus_or_thunderheads(cloud):
        if cloud == 0:
            return 1
        else:
            return 3
    if index == 0:
        return 100 - cumulus_or_thunderheads(c[index])
    while index != 0:
        count += cumulus_or_thunderheads(c[index])
        index += k
        if index >= len(c):
            index %= len(c)
        if index == 0:
            count += cumulus_or_thunderheads(c[index])
    return 100 - count

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''