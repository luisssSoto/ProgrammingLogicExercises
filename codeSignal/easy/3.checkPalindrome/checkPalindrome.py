def solution(inputString):
    completeList=list(inputString)
    middle=len(completeList)//2
    if len(completeList) % 2 != 0:
        completeList.pop(middle)
    firstPart=completeList[:middle]
    secondPart=completeList[middle:]
    secondPart.reverse()
    if firstPart == secondPart or len(completeList) == 1:
        result=True
    else:
        result=False
    return result 

print(solution('s0'))