def walls_and_gates(rooms: list[list[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    empty = 2147483647
    gate = 0
    m = len(rooms)
    if m == 0:
        return
    n = len(rooms[0])
    queue = []
    # adding position where the gate is to the queue
    for row in range(m):
        for col in range(n):
            if rooms[row][col] == gate:
                queue.append([row, col])
    directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]]
    while len(queue) > 0:
        point = queue.pop(0)
        row = point[0]
        col = point[1]
        for direction in directions:
            r = row + direction[0]
            c = col + direction[1]
            if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != empty:
                continue
            rooms[r][c] = rooms[row][col] + 1
            queue.append([r, c])
    print(f"rooms: {rooms}")

# Testcase
tc1 = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
walls_and_gates(tc1)