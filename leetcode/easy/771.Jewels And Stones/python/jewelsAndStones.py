"""Jewels And Stones"""

def num_jewels_in_stones(jewels: str, stones: str) -> int:
    my_stones = {}
    for stone in stones:
        if stone not in my_stones:
            my_stones[stone] = 1
        else:
            my_stones[stone] += 1
    my_jewels = 0
    for jewel in jewels:
        if jewel in my_stones:
            my_jewels += my_stones[jewel]
    return my_jewels

'''Complexity Analysis:
Time Complexity: O(N + M)
Space Complexity: O(N)'''

def num_jewesl_in_stones(jewels: str, stones: str) -> int:
    jewels = set(jewels)
    my_jewels = 0
    for stone in stones:
        if stone in jewels:
            my_jewels += 1
    return my_jewels

'''Complexity Analysis:
Time Complexity: O(N + M)
Space Complexity: O(N)'''

