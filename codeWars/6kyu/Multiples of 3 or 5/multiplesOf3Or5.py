def solution(number):
    if number > 0:
        multipleThree, multipleFive = 0, 0
        multipleList=[]
        result=0
        while multipleThree < number or multipleFive < number:
            multipleThree+=3
            multipleFive+=5
            if multipleThree < number:
                if multipleThree not in multipleList:
                    multipleList.append(multipleThree)
            if multipleFive < number:
                multipleList.append(multipleFive)
        for num in multipleList:
            result+=num
        return result
    else:
        return 0

print(solution(10))

            
