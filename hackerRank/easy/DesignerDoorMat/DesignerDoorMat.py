def welcome(high,width):
    element1=' . | . '
    count=0
    count1=3
    listElement1=[]
    while count != high:
        element1=element1.center(width,'-')
        listElement1=element1.split()
        print(listElement1)
        count+=1
                
welcome(5,15)