def likes(names):
    countNames=len(names)
    completeMsg=''
    msg='like this'
    if countNames == 0 or countNames == 1:
        newMsg=''
        for character in msg:
            if(character == ' '):
                character=character.replace(' ', 's ')
            newMsg+=character
        if countNames == 0:
            completeMsg+='no one ' + newMsg
        else:
            completeMsg+=names[0] + ' ' + newMsg
    elif countNames == 2:
        completeMsg = names[0] + ' and ' + names[1] + ' ' +  msg
    elif countNames == 3:
        completeMsg = names[0] + ', ' + names[1] + ' and ' + names[2] + ' ' + msg
    elif countNames > 3:
        completeMsg = names[0] + ', ' + names[1] + ' and ' + str(countNames-2) + ' others ' + msg
    return completeMsg

print(likes(['Joaquin', 'Pedro', 'Jackie', 'Gustavo', 'Adan', 'Leonel']))