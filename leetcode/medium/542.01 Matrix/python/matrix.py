"""01 Matrix"""

def matrix(mat: list[list[int]]) -> list[list][int]:
    from collections import deque

    matrix = mat[:]
    queue = deque()
    seen = set()
    rows = len(mat)
    cols = len(mat[0])

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                queue.append((r, c, 0))
                seen.add((r, c))
    
    def valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        row, col, steps = queue.popleft()
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            if (next_row, next_col) not in seen and valid(next_row, next_col):
                queue.append((next_row, next_col, steps + 1))
                seen.add((next_row, next_col))
                matrix[next_row][next_col] = steps + 1
    return matrix

'''Complexity Analysis:
Given m as the number of rows and n as the number of columns,
Time Complexity: O(m * n)
Space Complexity: O(m * n)'''

# testcase
t1 = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
t2 = [[0,0,0],[0,1,0],[1,1,1]]
print(matrix(t2))