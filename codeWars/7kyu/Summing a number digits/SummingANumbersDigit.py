def sum_digits(number):
    count = 0
    for character in str(number): 
        if character.isdigit(): count += int(character)
    return count

test1 = 10
test2 = 99
test3 = -32
print(sum_digits(test1))

'''Cleverest solution by: nickie'''
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))

print(abs(-3))