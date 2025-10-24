"""200.Number of Islands"""
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    islands = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == "1":
                islands += 1
                grid[row][col] = "0"
                neighboors = []
                neighboors.append((row, col))
                while neighboors:
                    r, c = neighboors.pop(0)
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        neighboors.append((r - 1, c))
                        grid[r - 1][c] = "0"
                    if r + 1 < num_rows and grid[r + 1][c] == "1":
                        neighboors.append((r + 1, c))
                        grid[r + 1][c] = "0"
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        neighboors.append((r, c -1))
                        grid[r][c - 1] = "0"
                    if c + 1 < num_cols and grid[r][c + 1] == "1":
                        neighboors.append((r, c + 1))
                        grid[r][c + 1] = "0"
    return islands
                        
"""Testcase"""
t1 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(num_islands(t1))

'''Complexity Analysis:
Time complexity: O(M * N) where M is the number of rows and
N is the number of columns.

Space complexity: O(min(M,N)) because in worst case where the
grid is filled with lands, the size of queue can grow up to min(M,N).'''