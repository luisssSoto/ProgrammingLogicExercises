"""Email Address Obfuscator"""
def obfuscate(email):
    #1. input a string email
    #   output a string with the (@ and .) 
    #   characters replaced by their literals inside a curly brackets ([at] and [dot])

    #2. find the special characters
    #   replace them for other ones

    #3. iterate for the email
    #   if the character is in the [@, .] so... and if the character is in [0] position so..
    #   replace the character with replace method ' [at] ' 
    #   else if the character in in the [1] position so...
    #   replace it with replace methof ' [dot] '
    #   assign that string to a new one
    #   return the new string

    #4. replace method replace all characters
    #   how to assing the characters to the new string
    key_characters = ['@', '.']
    for character in email:
        if character in key_characters:
            if character == key_characters[0]:
                email = email.replace('@', ' [at] ')
            else:
                email = email.replace('.', ' [dot] ')
        if key_characters[0] not in email and key_characters[1] not in email:
            break
    return email

test1 = 'jim.kuback@ennerman-hatano.com'
print(obfuscate(test1))


def obfuscate(email):
    dot_list = list(map(lambda character: character.replace('.', ' [dot] '), email))
    at_list = list(map(lambda character: character.replace('@', ' [at] '), dot_list))
    obfuscate_email = ''.join(at_list)
    return obfuscate_email

print(obfuscate(test1))

'''Cleverest solution by: CrazyMerlyn'''
def obfuscate(email):
    return email.replace("@", " [at] ").replace(".", " [dot] ")

