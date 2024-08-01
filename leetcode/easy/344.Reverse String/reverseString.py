"""Reverse String"""
def reverse_string(s):
    for i in range(len(s)//2):
        s[i], s[-1 - i] = s[-1 - i], s[i]
    return s

string_hello = "hello"
separacte_each_character = string_hello.replace('', ' ')
list_hello = separacte_each_character.split()
print(reverse_string(list_hello))

'''This could works also'''
x = [x for x in range(5)]
print(x)
x.reverse()
print(x)
'''
1. 
input: string  array
output string array but in reverse

2.
edge cases: nothing so far
key: perhaps I can convert the array into string first 
    iterate with a for loop the first element will be the last one and so on

3.
count = 1
for loop in range length // 2 then
    s[i], s[-count-i] = s[-count-i], s[i]
return s

4.
hello
helilo
'''