if __name__ == '__main__':
    s = input()
    def insideString(string):
        state=False
        l1=[]
        for i in range(len(string)):
            if string[i].isalnum():
                state=True
                l1.append(state)
            else:
                state=False
                l1.append(state)
        if True in l1:
            print(True)
        else:
            print(False)
        l2=[]
        for j in range(len(string)):
            if string[j].isalpha():
                state=True
                l2.append(state)
            else:
                state=False
                l2.append(state)
        if True in l2:
            print(True)
        else:
            print(False)
        l3=[]
        for k in range(len(string)):
            if string[k].isdigit():
                state=True
                l3.append(state)
            else:
                state=False
                l3.append(state)
        if True in l3:
            print(True)
        else:
            print(False)
        l4=[]
        for l in range(len(string)):
            if string[l].islower():
                state=True
                l4.append(state)
            else:
                state=False
                l4.append(state)
        if True in l4:
            print(True)
        else:
            print(False)
        l5=[]
        for m in range(len(string)):
            if string[m].isupper():
                state=True
                l5.append(state)
            else:
                state=False
                l5.append(state)
        if True in l5:
            print(True)
        else:
            print(False)
            
 
insideString('1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        
        