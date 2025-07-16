"""Diagonal Difference"""

def diagonal_difference(arr):
    operand1 = operand2 = cols1 = 0
    cols2 = len(arr) - 1
    for rows in range(len(arr)):
        operand1 += arr[rows][cols1]
        operand2 += arr[rows][cols2]
        cols1 += 1
        cols2 -= 1
    return abs(operand1 - operand2)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''