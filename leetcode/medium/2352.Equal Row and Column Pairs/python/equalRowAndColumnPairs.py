# 2352. Equal Row and Column Pairs

def equal_pairs(grid: list[list[int]]) -> int:
    ans = 0
    cols = {}
    rows = {}
    for row in grid:
        row = tuple(row)
        if row not in rows:
            rows[row] = 1
        else:
            rows[row] += 1
    col_idx = 0
    for i in range(len(grid)):
        col = []
        row_idx = 0
        for _ in range(len(grid[i])):
            col.append(grid[row_idx][col_idx])
            row_idx += 1
        col_idx += 1
        col = tuple(col)
        if col not in cols:
            cols[col] = 1
        else:
            cols[col] += 1
    for arr in rows:
        if arr in cols:
            ans += rows[arr] * cols[arr]
    return ans

grid1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
grid2 = [[11,1],[1,11]]
print(equal_pairs(grid1))

'''Complexity Analysis:
Time Complexity: O(N2)
Space Complexity: O(N2)'''