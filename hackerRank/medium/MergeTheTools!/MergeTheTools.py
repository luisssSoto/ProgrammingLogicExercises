def merge_the_tools(s,k):
    package=len(s)//k
    listStr=[]
    start=0
    end=0
    for i in range(package):
        column=[]
        for j in range(1):
            end+=k
            column.append(s[start:end])
            start+=k
        listStr.append(column)
    for k in listStr:
        for l in k:
            for m in range(len(l)):
                search=l.find(l[m],m+1)
                while search != -1:
                    print('find',l[m],'in index:',search)
                    search=l.find(l[m],m+=1)
            #     if l[m] in l[m+1:]:
            #         switch=True
            #         l.find(l[m])
            #         while 
            #         sustitution=l.replace(l[m],'',1)
            # if switch == True:
            #     print('sus',sustitution)
            # else:
            #     print(l)
        
merge_the_tools('AAABCADDE',3)
        