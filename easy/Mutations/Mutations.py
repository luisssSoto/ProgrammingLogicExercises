def mutate_string(string, position, character):
    '''
    first way:
    listString=list(string)
    listString[position]=character
    string=''.join(listString)
    return string'''
'''
second way:
    string=string[:position]+character+string[position+1:]
    return string'''

'''last way:
    liString=list(string)
    liString.pop(position)
    liString.insert(position,character)
    string=liString
    string="".join(string)
    return string'''
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)