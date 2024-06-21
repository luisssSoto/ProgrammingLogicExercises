def solution(matrix):
    building_columns = []
    count = 0
    total = 0
    if len(matrix) > 1:
        while count <= len(matrix):
            column = []
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if j == count:
                        column.append(matrix[i][j])
                        break
            building_columns.append(column)
            count += 1
        for list in building_columns:
            for element in list:
                if element == 0:
                    break
                else:
                    total += element 
    else:
        for list in matrix:
            for element in list:
                total += element   
    return total
                
matrix = [[1,2,3,4,5]]
test = [[0,1,1,2],[0,5,0,0],[2,0,3,3]]
print(solution(matrix))