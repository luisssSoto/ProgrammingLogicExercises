"""Utopian Tree"""

def utopian_tree(n: int) -> int:
    height = 0
    for i in range(n + 1):
        if i % 2 == 0:
            height += 1
        else:
            height += height
    return height

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''