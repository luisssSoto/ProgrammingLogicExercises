"""Super Reduced String"""

def super_reduced_string(s: str) -> str:
    stack = []
    for letter in s:
        stack.append(letter)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        return "Empty String"
    else:
        return ''.join(stack)
    
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''