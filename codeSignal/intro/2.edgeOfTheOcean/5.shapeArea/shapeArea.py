def solution (n):
    centerRow=n+n-1
    count=0
    area=centerRow
    square=1
    newRow=centerRow
    while  square <= centerRow-2:
        square+=2
        count+=1
    for i in range(count):
        newRow-=2
        firstPart=newRow
        lastPart=newRow
        area+=firstPart+lastPart
    return area

print(solution(4))