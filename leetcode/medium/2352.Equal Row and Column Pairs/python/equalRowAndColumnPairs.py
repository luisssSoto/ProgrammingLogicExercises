# 2352. Equal Row and Column Pairs

def equal_pairs(grid: list[list[int]]) -> int:
    from collections import defaultdict
    ans = 0
    rows = defaultdict(int)
    for row in grid:
        rows[tuple(row)] += 1
    cols = defaultdict(int)
    for col in range(len(grid[0])):
        new_col = []
        for row in range(len(grid)):
            new_col.append(grid[row][col])
        cols[tuple(new_col)] += 1
    for arr in rows:
        ans += rows[arr] * cols[arr]
    return ans

grid1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
grid2 = [[11,1],[1,11]]
print(equal_pairs(grid1))

'''Complexity Analysis:
Time Complexity: O(N2)
Space Complexity: O(N2)'''