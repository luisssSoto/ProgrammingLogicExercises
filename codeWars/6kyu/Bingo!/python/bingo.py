"""Bingo!"""
def bingo(card, numbers):
    winners = []
    col_b = []
    col_i = []
    col_n = []
    col_g = []
    col_o = []
    dia_left = []
    dia_right = []
    for row in range(1, len(card)):
        r = []
        for col in range(len(card[row])):
            if col == 0:
                num = "B" + str(card[row][col])
                col_b.append(num)
                if row == 1:
                    dia_left.append(num)
                elif row == 5:
                    dia_right.append(num)
            elif col == 1:
                num = "I" + str(card[row][col])
                col_i.append(num)
                if row == 2:
                    dia_left.append(num)
                elif row == 4: 
                    dia_right.append(num)
            elif col == 2:
                num = "N" + str(card[row][col])
                col_n.append(num)
                if row == 3:
                    dia_left.append(num)
                if row == 3: 
                    dia_right.append(num)
            elif col == 3:
                num = "G" + str(card[row][col])
                col_g.append(num)
                if row == 4:
                    dia_left.append(num)
                elif row == 2: 
                    dia_right.append(num)
            else:
                num = "O" + str(card[row][col])
                col_o.append(num)
                if row == 5:
                    dia_left.append(num)
                elif row == 1: 
                    dia_right.append(num)
            r.append(card[0][col] + str(card[row][col]))
        winners.append(r)
    winners.append(col_b)
    winners.append(col_i)
    winners.append(col_n)
    winners.append(col_g)
    winners.append(col_o)
    winners.append(dia_left)
    winners.append(dia_right)
    print(winners)
    for row in winners:
        count = 0
        for num in row:
            if num in numbers or num == "NFREE SPACE":
                count += 1
            else:
                break
            if count == 5:
                return True
    return False

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''