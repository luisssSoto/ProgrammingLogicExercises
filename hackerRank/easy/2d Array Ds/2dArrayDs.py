"""2d Array DS"""
def hourglass_sum(arr):
    hourglass_list = []
    for i in range(4):
        for j in range(4):
            start_sum = 0
            for k in range(3):
                start_sum += arr[i][k + j]
                start_sum += arr[i + 2][k + j]
            start_sum += arr[i + 1][j + 1]
            hourglass_list.append(start_sum)
    return max(hourglass_list)

data1 = [
    [-9, -9, -9,  1, 1, 1],
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]
    ]

print(hourglass_sum(data1))
'''
1.
input: 2d array
output: integer as a result of the greater hourglase sum

2.
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

edge cases: are not so far
key: 2d array: 6 * 6 = 16 combinations
create a list to save all the hourglasses sum

iterate with a for loop
create a count = 3
create a second count = 1
create a third count = 3
for range 16
column = 0
for j in range 4
    sum += 
    for k in range 12
    sum += arr[i][k]
    sum += arr[i + 2][k]
sum += arr[i + 1][second_row]
second_row +=1


'''