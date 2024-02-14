def solution(n):
    strNumbers=str(n)
    result=0
    for strNumber in strNumbers:
        intNumber=int(strNumber)
        result+=intNumber
    return(result)

print(solution(210))