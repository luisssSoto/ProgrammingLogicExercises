"""Baseball Game"""

def calPoints(operations: list[str]) -> int:
    stack = []
    result = 0
    for operation in operations:
        if operation == "+":
            stack.append(int(stack[-1] + stack[-2]))
            result += stack[-1]
        elif operation == "C":
            result -= stack[-1]
            stack.pop()
        elif operation == "D":
            stack.append(int(stack[-1] * 2))
            result += stack[-1]
        else:
            stack.append(int(operation))
            result += stack[-1]
    return result

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''