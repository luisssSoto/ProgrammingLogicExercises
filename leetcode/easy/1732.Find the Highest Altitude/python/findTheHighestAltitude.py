# 1732. Find the Highest Altitude

def largest_altitude(gain: list[int]) -> int:
    max_alt = curr_sum = 0
    for alt in gain:
        curr_sum += alt
        max_alt = max(max_alt, curr_sum)
    return max_alt

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''