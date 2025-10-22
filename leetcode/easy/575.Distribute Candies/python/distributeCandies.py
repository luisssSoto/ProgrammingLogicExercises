"""Distribute Candies"""
def distribute_candies(candyType: list[int]) -> int:
    types_candies = set(candyType)
    candies = len(candyType) // 2
    if len(types_candies) >= candies:
        return candies
    else:
        return len(types_candies)
    
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''