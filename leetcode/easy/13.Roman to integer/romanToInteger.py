"""13.Roman to Integer"""
def roman_to_integer(s):
    roman_integer = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    decimal = 0
    if "IV" in s:
        s = s.replace("IV", '')
        decimal += 4
    if "IX" in s:
        s = s.replace("IX", "")
        decimal += 9
    if "XL" in s:
        s = s.replace("XL", "")
        decimal += 40
    if "XC" in s:
        s = s.replace("XC", "")
        decimal += 90
    if "CD" in s:
        s = s.replace("CD", "")
        decimal += 400
    if "CM" in s:
        s = s.replace("CM", "")
        decimal += 900
    for roman in s:
        decimal += roman_integer[roman]
    return decimal

s = "III"
s1 = "LVIII"
s2 = "MCMXCIV"
print(roman_to_integer(s2))

roman_integer = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }




'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.'''

'''
1.
input: string
output: integer which is result of the convertion from decimal number to roman number

2.
edge cases: if it is 4, 9, 40, 90, 400, 900
key: data structure: dictionary
iterate string with for loop element by element
create a list in order to decode all roman into decimal number
create an integer variable to sum
return the integer variable

3. 
dict = {roman = decimal}
replace the values that are an exception
sum it to the variable count and then
for element in string then
     sum to the cound depends the dict

4. 


'''