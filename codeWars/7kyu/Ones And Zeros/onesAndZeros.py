def binary_array_to_number(arr):
    length = len(arr) - 1
    decimal_number = 0
    for number in arr:
        if number == 1: decimal_number += 2 ** length
        length -= 1
    return decimal_number
        
array = [0, 1, 0, 1]
print(binary_array_to_number(array))

#Cleverest
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)
