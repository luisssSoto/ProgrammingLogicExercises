def x(n: int) -> list[list[int]]:
    is_it_odd = n % 2 != 0
    num_rows = n // 2
    if is_it_odd is True:
        num_rows += 1
    last_pointer = n - 1
    matrix = []
    for i in range(num_rows):
        row = [0 for x in range(n)]
        for j in range(n):
            if j == i or j == last_pointer:
                row[j] = 1
        last_pointer -= 1
        matrix.append(row)
    last_rows = len(matrix) - 1
    if is_it_odd is True:
        last_rows -= 1
    for i in range(last_rows, -1, -1):
        matrix.append(matrix[i])
    return matrix

'''Complexity Analysis:
Time Complexity: O(N + M)
Space Complexity: O(N + M)'''