"""Roman Numerals Encoder"""
def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    roman_dict = {
        "MMM" : 3000,
        "MM" : 2000,
        "M" : 1000,
        "CM" : 900,
        "DCCC" : 800,
        "DCC" : 700,
        "DC" : 600,
        "D" : 500,
        "CD" : 400,
        "CCC" : 300,
        "CC" : 200,
        "C" : 100,
        "XC" : 90,
        "LXXX" : 80,
        "LXX" : 70,
        "LX" : 60,
        "L" : 50,
        "XL" : 40,
        "XXX" : 30,
        "XX" : 20,
        "X" : 10,
        "IX" : 9,
        "VIII" : 8,
        "VII" : 7,
        "VI" : 6,
        "V" : 5,
        "IV" : 4,
        "III" : 3,
        "II" : 2,
        "I" : 1
    }
    roman_str = ""
    dec_int = 0
    tortoise = hare = 0
    while hare != len(roman):
        if roman[tortoise] == "M":
            for i in range(hare, len(roman)):
                if roman[hare] != "M":
                    roman_str = roman[tortoise : hare]
                    dec_int += roman_dict[roman_str]
                    tortoise = hare
                    break
                hare += 1
        if tortoise == len(roman):
            return dec_int
        if roman[tortoise] == "C" or roman[tortoise] == "D":
            for i in range(hare, len(roman)):
                if roman[hare] != "C" and roman[hare] != "D" and roman[hare] != "M":
                    roman_str = roman[tortoise : hare]
                    dec_int += roman_dict[roman_str]
                    tortoise = hare
                    break
                hare += 1
        if tortoise == len(roman):
            return dec_int
        if roman[tortoise] == "X" or roman[tortoise] == "L":
            for i in range(hare, len(roman)):
                if roman[hare] != "X" and roman[hare] != "L" and roman[hare] != "C":
                    roman_str = roman[tortoise : hare]
                    dec_int += roman_dict[roman_str]
                    tortoise = hare
                    break
                hare += 1
        if tortoise == len(roman):
            return dec_int
        roman_str = roman[tortoise : ]
        dec_int += roman_dict[roman_str]
        return dec_int

'''Complexity Analysis:
Time Complexity: O(N) 
Space Complexity: O(N)
'''