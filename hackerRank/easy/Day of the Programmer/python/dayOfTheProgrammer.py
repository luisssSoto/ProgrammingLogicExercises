"""Day of the Programmer"""

def day_of_programmer(year: int) -> str:
    date = ""
    if year <= 1917:
        if year % 4 == 0:
            date = "12"
        else:
            date = "13"
    elif year == 1918:
        date = "26"
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            date = "12"
        else:
            date = "13"
    date += ".09." + str(year)
    return date

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''