def solution(inputArray):
    largestProduct=-999_999_999
    for operator in range(len(inputArray)-1):
        result=inputArray[operator]*inputArray[operator+1]
        if result > largestProduct:
            largestProduct=result
    return largestProduct

#create a variable calls largestProduct
# iterar in the array
#return largest adjacent elments product
largestNumber=solution([3,6,-2,-5,7,3])
print(largestNumber)