list1=[]

#Define functions
def insertFunction(li,position,value):
    li.insert(position, value)
def printFunction(li):
    print(li)
def removeFunction(li,value):
    li.remove(value)
def appendFunction(li,value):
    li.append(value)
def sortFunction(li):
    li.sort()
def popFunction(li):
    li.pop()
def reverseFunction(li):
    li.reverse()

#Define main function which set the list element
def setList(numberFunctions):
    for i in range(numberFunctions):
        callFunction=input("What function do you want to use?")
        if callFunction.startswith("insert"):
            lis=callFunction.split()
            elementPosition=int(lis[-2])
            elementValue=int(lis[-1])
            insertFunction(list1,elementPosition,elementValue)
        if callFunction.startswith("print"):
            printFunction(list1)
        if callFunction.startswith("remove"):
            lis=callFunction.split()
            removeValue=int(lis[-1])
            removeFunction(list1,removeValue)
        if callFunction.startswith("append"):
            lis=callFunction.split()
            appendValue=int(lis[-1])
            appendFunction(list1,appendValue)
        if callFunction.startswith("sort"):
            sortFunction(list1)
        if callFunction.startswith("pop"):
            popFunction(list1)
        if callFunction.startswith("reverse"):
            reverseFunction(list1)

#Calling the function
numberFunctions=int(input("How many functions do you want to use?"))
setList(numberFunctions)

