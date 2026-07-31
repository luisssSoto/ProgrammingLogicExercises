# First Letter To Appear Twice

def repeated_character(s: str) -> str:
    unique_vals = set()
    for ch in s:
        if ch in unique_vals:
            return ch
        unique_vals.add(ch)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(n)'''