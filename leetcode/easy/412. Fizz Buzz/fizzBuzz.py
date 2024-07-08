"""FizzBuzz"""
def fizzBuzz(n):
    fizz_buzz_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append('FizzBuzz')
        elif i % 3 == 0:
            fizz_buzz_list.append('Fizz')
        elif i % 5 == 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(str(i))
    return fizz_buzz_list

test1 = 15
print(fizzBuzz(test1))
#1. input: integer
#   output: integer array

#2. create an empty lis
#   iterate from 1 to range(n)
#   conditionals
#   append the value according the conditionals
#   return the list

#3. new_list = []
#   for x in range(1, n + 1):
#   conditionals
#   append the value according the condtionals
#   return the list

#4. ready to Code