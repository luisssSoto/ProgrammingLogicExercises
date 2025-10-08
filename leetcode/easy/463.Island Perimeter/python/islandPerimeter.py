"""Island Perimeter"""

def island_perimeter(grid: list[list[int]])-> int:
    lands = 0
    lands_append = 0
    for row in grid:
        for square in row:
            if square == 1:
                lands += 1
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == 1 and grid[i][j + 1] == 1:
                lands_append += 2
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and grid[i - 1][j] == 1:
                lands_append += 2
    return lands * 4 - lands_append

'''Complexity Analysis:
Time Complexity: O(M * N)
Space Complexity: O(N)'''