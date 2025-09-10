"""Valid Sudoku"""
# Approach 1:
def is_valid_sudoku(board):
        columns = {}
        first_square = []
        second_square = []
        thirdth_square = []
        for i in range(len(board)):
            row = []
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    row.append(board[i][j])
                elif board[i][j] not in row:
                    row.append(board[i][j])
                elif board[i][j] in row:
                    return False
                if board[i][j] != ".":
                    if board[i][j] not in columns:
                        columns[board[i][j]] = []
                        columns[board[i][j]].append(j)
                    elif board[i][j] in columns:
                        if j in columns[board[i][j]]:
                            return False
                        else:
                            columns[board[i][j]].append(j)
            first_square += row[:3]
            second_square += row[3:6]
            thirdth_square += row[6:]
            if i == 2 or i == 5 or i == 8:
                for x in range(len(first_square) - 1):
                    if first_square[x] == ".":
                        continue
                    if first_square[x] in first_square[x + 1:]:
                        return False
                for x in range(len(second_square) - 1):
                    if second_square[x] == ".":
                        continue
                    if second_square[x] in second_square[x + 1:]:
                        return False
                for x in range(len(thirdth_square) - 1):
                    if thirdth_square[x] == ".":
                        continue
                    if thirdth_square[x] in thirdth_square[x + 1:]:
                        return False
                first_square = []
                second_square = []
                thirdth_square = []
        return True

'''Complexity Analsyis:
Time Complexity: O(N2)
Space Complexity: O(N)'''

# Approach 2: 
def is_valid_sudoku(board):
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(is_valid_sudoku(sudoku))


'''Complexity Analsyis:
Time Complexity: O(N2)
Space Complexity: O(N2)'''