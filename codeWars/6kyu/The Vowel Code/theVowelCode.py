# 07:53
# 08:34

def encode(word):
    # create a dictionary which keeps the rules of vowels
    codingDict = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
    # create a string variable to save the coding value
    encodeWord = ''
    # iterate through the word
    for letter in word:
    # conditional if the element in dictionary so:
        if letter in codingDict:
    # use replace function to replace that element for its equivalent number according to the dictionary
            encodeLetter = codingDict[letter]
    # and that value add to string variable
            encodeWord += encodeLetter
    # conditional else to add that element to the string variable
        else:
            encodeWord += letter
    return encodeWord
# repeate the same proccess but codingDict will be in reverse

def decode(word):
    codingDict = {'1':'a', '2':'e', '3':'i', '4':'o', '5':'u'}
    decodeWord = ''
    for character in word:
        if character in codingDict:
            decodeLetter = codingDict[character]
            decodeWord += decodeLetter
        else:
            decodeWord += character
    return decodeWord

print(encode('hello'))
print(decode('h2ll4'))