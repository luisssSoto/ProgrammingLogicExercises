""" Simple Pig Latin """
def pig_it(text):
    listText = text.split(' ')
    for i in range(len(listText)):
        if listText[i].isalpha() == True:
            firstCharacter = listText[i][0]
            newWord = listText[i].replace(firstCharacter, '', 1) + firstCharacter + 'ay'
            listText[i] = newWord
    strText = ' '.join(listText)
    return strText
