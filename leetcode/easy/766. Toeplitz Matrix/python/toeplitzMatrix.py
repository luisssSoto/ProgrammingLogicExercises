"""Toeplitz Matrix"""

# Approach 1
def toeplitz_matrix(matrix: list[list[int]]) -> bool:
    max_col = len(matrix[0]) - 1
    max_ele = min(len(matrix), len(matrix[0]))
    count_col = 1
    result = False
    for c in range(max_col, -1, -1):
        r = 0
        i = 0
        first = matrix[r][c]
        while i < count_col:
            val = matrix[r][c]
            if first != val:
                return result
            i += 1
            r += 1
            c += 1
        count_col += 1
        if count_col > max_ele:
            count_col = max_ele
    max_row = len(matrix) - 1
    count_row = 1
    for r in range(max_row, 0, -1):
        c = 0
        i = 0
        first = matrix[r][c]
        while i < count_row:
            val = matrix[r][c]
            if val != first:
                return result
            i += 1
            r += 1
            c += 1
        count_row += 1
        if count_row > max_ele:
            count_row = max_ele
    result = True
    return result

'''Complexity Analysis:
Time Complexity: O(M * N)
Space Complexity: O(N)'''

# Testcases
t1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
t2 = [[x for x in range(2)] for _ in range(5)]
t3 = [[1,2],[2,2]]
print(toeplitz_matrix(t1))
print(toeplitz_matrix(t2))
print(toeplitz_matrix(t3))

# Approach 2
def toeplitz_matrix(matrix: list[list[int]]) -> bool:
    groups = {}
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if r - c not in groups:
                groups[r - c] = val
            elif groups[r - c] != val:
                return False
    return True

'''Complexity Analysis:
Time Complexity: O(M * N)
Space Complexity: O(N)'''

