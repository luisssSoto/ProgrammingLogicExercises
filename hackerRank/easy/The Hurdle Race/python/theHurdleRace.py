"""The Hurdle Race"""

def hurdle_race(k, height):
    # Write your code here
    max_val = max(height)
    if max_val - k <= 0:
        return 0
    else:
        return max_val - k
    
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''