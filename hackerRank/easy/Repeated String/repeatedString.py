def repeated_string(s, n):
    amount_a = 0
    if s == 'a':
        return n
    for letter in s:
        if letter == 'a':
            amount_a += 1
    amount_a *= n // len(s)
    last_characters = n % len(s)
    if last_characters != 0:
        last_string = s[:last_characters]
        for letter in last_string:
            if letter == 'a':
                amount_a += 1
    return amount_a
string = 'aba'
integer = 10
print(repeated_string(string, integer))
'''
1.
input: string and integer
output: integer that counts all the a after modifying the string
    
2.
edge cases: if there is any 'a' return 0
not form the entire string
key: it is only a formula
    
3. 
count how many 'a's are in the intial string
entire division to know how many times all the string is repeated
multiply the first value between the second one
now use module operation % in order to know how many characters less
form an string and then count a
iterable for loop
sum this last value between the first one an return it
    
4.
happy coding!
    
'''

l = [chr(x) for x in range(98, 102)]
print(l)
h = 'helloe'
h.find('e', 1)