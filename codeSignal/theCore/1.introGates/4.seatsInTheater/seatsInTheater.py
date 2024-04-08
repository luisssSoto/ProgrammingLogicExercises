#time started: 11:00
def solution(nCols, nRows, col, row):
    nRows -= row
    nCols -= col
    nCols += 1
    return nRows * nCols

print(solution(16,11,5,3))