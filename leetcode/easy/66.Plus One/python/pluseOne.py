"Plus One"

def plus_one(digits):
    final_digits = []
    digits_str = ''
    for digit in digits:
        digits_str += str(digit)
    digits_int = int(digits_str)
    digits_int += 1
    print(f'int: {digits_int}')
    digits_str = str(digits_int)
    for i in range(len(digits_str)):
        final_digits.append(int(digits_str[i]))
    return final_digits

# Testing
digits1 = [7,2,3]
digits2 = [9]
print(plus_one(digits1))