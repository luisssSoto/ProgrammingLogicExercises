"""Sqrt """

def my_sqrt(x):
    operand = 0
    while True:
        result = operand * operand
        if result > x:
            return operand - 1
        elif result == x:
            return operand
        operand += 1

# Testing 
data_1 = 4
data_2 = 8
print(my_sqrt(data_2))

'''Complexity Analysis:
Time Complexity: O(Sqrt(x))
Space Complexity: O(1)'''

# Approach 2: Binary Search
def my_sqrt(x):
    def helper(x):
        left_pointer = 0
        right_pointer = x
        middle_pointer = 0
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2 
            if middle_pointer * middle_pointer == x:
                return middle_pointer
            elif middle_pointer * middle_pointer > x:
                middle_pointer -= 1
                right_pointer = middle_pointer
            elif middle_pointer * middle_pointer < x:
                middle_pointer += 1
                left_pointer = middle_pointer
        return middle_pointer
    sqrt_num = helper(x)
    if sqrt_num * sqrt_num > x:
        return sqrt_num - 1
    else:
        return sqrt_num
data_1 = 4
data_2 = 8
data_3 = 3
data_4 = 16
print(my_sqrt(data_4))

'''Complexity Analysis:
Time Complexity: O(log)
Space Complexity: O(1)'''

