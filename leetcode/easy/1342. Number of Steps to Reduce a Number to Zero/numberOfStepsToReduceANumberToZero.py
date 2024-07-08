"""Number of Steps to Reduce a Number to Zero"""
def number_of_steps(num):
    count = 0
    while num != 0:
        if num % 2 == 0: num //= 2
        else: num -= 1
        count += 1
    return count

test1 = 123
print(number_of_steps(test1))        

#1. input: integer
#   output: integer

#2. while until n different zero
#   conditional for even and odd number
#   variable to count every time any conditional executes
#   return the count

#3. while n != 0 continue...
#   if n % 2 == 0 then..
#   n //= 2 
#   increase count to 1
#   else:
#   n -= 1
#   increase count to 1
#   return count

#4. doub about while, be careful