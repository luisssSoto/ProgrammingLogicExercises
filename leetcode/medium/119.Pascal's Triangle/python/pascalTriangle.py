"""Pascal's Triangle"""

def pascal_triangle(rowIndex):
    """Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle."""
    row_pascal = [1]
    for i in range(rowIndex):
        n = len(row_pascal)
        row_pascal.insert(0, 0)
        row_pascal.append(0)
        for j in range(n):
            value = row_pascal[j] + row_pascal[j + 1]
            row_pascal[j] = value
        del row_pascal[-1]
    return row_pascal

# Testing
row_index0 = 3
row_index1 = 0
row_index2 = 1
print(pascal_triangle(row_index2))

'''Complexity Analysis:
Time Complexity: O(rowIndex2)
Space Complexity: O(rowIndex)'''