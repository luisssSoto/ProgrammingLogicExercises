# Enter your code here. Read input from STDIN. Print output to STDOUT

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

#Create a list for the lines of number
#Create another one inside it
#Create three Strings variables
def welcome(rows, cols):
    w=''
    for row in range(rows):
        r=''
        c=''
        for col in range(cols):
            c+='-'
        r+=c
        w+=r
    return w

print(welcome(5,15))
