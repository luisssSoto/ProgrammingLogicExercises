"""Decode String"""

def decodeString(s: str) -> str:
    stack = []
    for i in range(len(s)):
        if s[i] == "]":
            decoded_str = ""
            while stack[-1] != "[":
                decoded_str += stack.pop()
            stack.pop()
            base = 1
            k = 0
            while stack and stack[-1].isdigit():
                k = k + (int(stack.pop())) * base
                base *= 10
            decoded_str = decoded_str * k
            for i in range(len(decoded_str) - 1, -1, -1):
                stack.append(decoded_str[i])
        else:
            stack.append(s[i])
    return "".join(stack)

t = "3[a2[cd]]"
print(decodeString(t))

'''Complexity Analysis:
Time Complexity: O(maxK **countK *n)
Space Complexity: O(∑(maxK **countK *n))'''

