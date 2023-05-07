def textWrap(string,max_width):
    countBegin=0
    countFinal=0
    count=0
    newString=''
    for i in range(len(string)):
        countFinal+=max_width
        newString+= string[countBegin:countFinal]+"\n"
        countBegin+=max_width
    return newString.rstrip()

print(textWrap('HackerRank',2))