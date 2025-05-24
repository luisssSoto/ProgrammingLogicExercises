"Two Sum II - Input Array is Sorted"
# My Approach
def two_sum_II(numbers, target):
    right_indexes = []
    for operand_pointer_1 in range(len(numbers) - 1):
        operand_pointer_2 = operand_pointer_1 + 1
        if numbers[operand_pointer_1] == numbers[operand_pointer_2] and numbers[operand_pointer_1] + numbers[operand_pointer_2] != target:
            continue
        while operand_pointer_2 < len(numbers):
            result = numbers[operand_pointer_1] + numbers[operand_pointer_2]
            if result == target:
                right_indexes.append(operand_pointer_1 + 1)
                right_indexes.append(operand_pointer_2 + 1)
                return right_indexes
            elif result > target:
                break
            operand_pointer_2 += 1

# Testing
n0 = [2,7,11,15]
t0 = 9
n1 = [2,3,4]
t1 = 6
n2 = [-1, 0]
t2 = -1
n3 = [5,25,75]
t3 = 100
n4 = [3,24,50,79,88,150,345]
t4 = 200
n5 = [-1 for x in range(198)]
n5.append(1)
n5.append(1)
t5 = 2
n6 = [-1,-1] + [1 for x in range(198)]
t6 = -2
print(two_sum_II(n6, t6))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Approach 1: Two Pointers
def twoSumII(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1
    sum_indexes = [-1, -1]
    while left_pointer < right_pointer:
        result = numbers[left_pointer] + numbers[right_pointer]
        if result == target:
            sum_indexes = [left_pointer + 1, right_pointer + 1]
            return sum_indexes
        elif result > target:
            right_pointer -= 1
        else:
            left_pointer += 1
    return sum_indexes