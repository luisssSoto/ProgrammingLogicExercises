def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    '''Stack Approach'''
    if image[sr][sc] == color:
        return image
    def move(pos):
        x = pos[0]
        y = pos[1]
        if x > 0:
            if image[x - 1][y] == original_col and image[x - 1][y] not in visited:
                stack.append((x - 1, y))
                visited.add((x - 1, y))
                image[x - 1][y] = color
        if y < len(image[0]) - 1:
            if image[x][y + 1] == original_col and image[x][y + 1] not in visited:
                stack.append((x, y + 1))
                visited.add((x, y + 1))
                image[x][y + 1] = color
        if x < len(image) - 1:
            if image[x + 1][y] == original_col and image[x + 1][y] not in visited:
                stack.append((x + 1, y))
                visited.add((x + 1, y))
                image[x + 1][y] = color
        if y > 0:
            if image[x][y - 1] == original_col and image[x][y - 1] not in visited:
                stack.append((x, y - 1))
                visited.add((x, y - 1))
                image[x][y - 1] = color
    stack = [(sr, sc)]
    visited = set()
    visited.add((sr, sc))
    original_col = image[sr][sc]
    image[sr][sc] = color
    while stack:
        curr = stack.pop()
        move(curr)
    return image

def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    '''DFS Approach'''
    R, C = len(image), len(image[0])
    new_color = image[sr][sc]
    if new_color == color:
        return image
    def dfs(r, c):
        if image[r][c] == new_color:
            image[r][c] = color
            if r >= 1:
                dfs(r-1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity O(N)'''