"""ROT 13"""
def rot13(message):
    rot13_message = ''
    for character in message:
        if character.isalpha():
            code_character = ord(character)
            code_character += 13
            if character.islower():
                if code_character > ord('z'):
                    code_character %= ord('z')
                    code_character += ord('a') - 1
            elif character.isupper():
                if code_character > ord('Z'):
                    code_character %= ord('Z')
                    code_character += ord('A') - 1
            code_character = chr(code_character)
            rot13_message += code_character
        else:
            rot13_message += character
    return rot13_message

test = 'EBG13 rknzcyr.'
test1 = 'This is my first ROT13 excercise!'
print(rot13(test))
