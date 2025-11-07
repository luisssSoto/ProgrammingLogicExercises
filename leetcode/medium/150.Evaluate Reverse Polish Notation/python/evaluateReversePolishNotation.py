"""Evaluate Reverse Polish Notation"""

def evalRPN(tokens: list[str]) -> int:
    operands = []
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)
    }
    for token in tokens:
        if token not in operations:
            operands.append(int(token))
        else:
            second_operand = operands.pop()
            first_operand = operands.pop()
            result = operations[token](first_operand, second_operand)
            operands.append(result)
    return operands[-1]

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''