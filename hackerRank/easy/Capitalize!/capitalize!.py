def solve(s):
    uppercaseName=''
    positionFirstLetter=[]
    sList=list(s)
    sList[0]=sList[0].upper()
    for i in range(len(s)):
        if s[i] == ' ':
            positionFirstLetter.append(i+1)
    for position in positionFirstLetter:
        uppercaseLetter=sList[position].upper()
        sList[position]=uppercaseLetter
    for character in sList:
        uppercaseName+=character
    return uppercaseName

test='test1'
print(test.index('e'))
        
print(solve('leonardo dicaprio'))