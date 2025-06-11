"""Valid Parentheses"""

def valid_parentheses(s):
    stack = []
    mapping = {")" : "(", "]" : "[", "}" : "{"}
    for chr in s:
        if chr in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[chr] != top_element:
                return False
        else:
            stack.append(chr)
    return not stack

# Testing 
s = "([])"
print(valid_parentheses(s))


'''Complexity analysis
Time complexity : O(n) because we simply traverse the given 
string one character at a time and push and pop operations 
on a stack take O(1) time.
Space complexity : O(n) as we push all opening brackets onto 
the stack and in the worst case, we will end up pushing all 
the brackets onto the stack. e.g. ((((((((((.
'''