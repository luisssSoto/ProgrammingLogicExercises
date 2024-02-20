
def print_rangoli(size):
    alphabet='a b c d e f g h i j k l m n o p q r s t u v w x y z'
    listAlphabet=alphabet.split()
    keyValue=size-1
    firstLetter=listAlphabet[keyValue]
    specialCharacter='-'

    letters=size*2-1
    characters=letters-1
    elementsInRow=letters+characters
    middleElement=elementsInRow//2

    firstList=[specialCharacter if (i != middleElement) else firstLetter for i in range(elementsInRow)]
    firstPartList=[firstList for j in range(1)]
    for k in range(keyValue):
        otherList=firstPartList[k][:]
        justMiddle=len(otherList)//2
        middleLetter=otherList[justMiddle]
        positionLeft=justMiddle
        positionRight=positionLeft+1
        
        otherList.insert(positionLeft, specialCharacter)
        otherList.insert(positionLeft, middleLetter)
        del otherList[0]
        del otherList[0]
        otherList.insert(positionRight, middleLetter)
        otherList.insert(positionRight, specialCharacter)
        del otherList[-1]
        del otherList[-1] 
        
        otherList[justMiddle]=listAlphabet[size-2-k]
        firstPartList.append(otherList)
    
    secondPartList=firstPartList[:]
    secondPartList.reverse()
    positionRowDel=size*2//2
    finalList=firstPartList+secondPartList
    del finalList[positionRowDel]
    strList=''
    for row in finalList:
        for position in range(len(row)):
            strList+=row[position]
            if position == len(row)-1:
                strList+='\n'
    print(strList)

print_rangoli(10)


