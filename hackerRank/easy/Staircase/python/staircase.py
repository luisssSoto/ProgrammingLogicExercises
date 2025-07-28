"""Staircase"""

def staircase(n):
    stair = [" " if x < n - 1 else "#" for x in range(n)]
    for i in range(n):
        print("".join(stair))
        stair.pop(0)
        stair.append("#")
        
# Testing
staircase(6)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''