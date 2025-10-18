"""Reshape the Matrix"""

def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    queue = [cell for row in mat for cell in row]
    result = [[None for _ in range(c)]for _ in range(r)]
    for i in range(len(result)):
        for j in range(len(result[i])):
            if len(queue) == 0:
                return mat
            result[i][j] = queue.pop(0)        
    if result[-1][-1] != mat[-1][-1]:
        return mat
    else:
        return result
    
'''Complexity Analysis:
Time Complexity: O(M * N)
Space Complexity: O(M * N)'''