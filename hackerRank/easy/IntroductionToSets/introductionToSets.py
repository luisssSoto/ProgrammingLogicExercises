#Time started 09:54
#Finish it 10:15
def average(array):
    setArray = set(array)
    lengthArray = len(setArray)
    sumElementsArray=0
    averageArray=0
    for element in setArray:
        sumElementsArray += element
    averageArray = sumElementsArray / lengthArray
    return averageArray

a=[161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
print(average(a))

setA = set(a)
print(setA)
print(type(setA))
setArray = {'h', 'e', 'l', 'l', 'o', 1}
print(setArray)