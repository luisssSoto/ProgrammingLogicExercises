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

def romand_to_int(s: str) -> int:
    roman_dec = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    dec = roman_dec[s[-1]]
    for i in range(len(s) - 1):
        if roman_dec[s[i]] < roman_dec[s[i + 1]]:
            dec -= roman_dec[s[i]]
        else:
            dec += roman_dec[s[i]]
    return dec

'''Complexity Analysis:
Time Complexity: O(1) Because the constraints the larger number is 3999
Space Complexity: O(1)'''