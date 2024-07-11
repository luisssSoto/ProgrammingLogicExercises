"""Find Numbers With Even Number of Digits"""
def find_numbers(nums):
    even_counter = 0
    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0: even_counter += 1
    return even_counter

test1 = [12,345,2,6,7896]
test2 = [555,901,482,1771]
print(find_numbers(test2))

#1. input: array
#   output: the amount of numbers which have only even number of digits

#2. length of every element of the list
#   variable counter to count the number of digits of every element
#   iterate with a for loop through the array
#   cast each element in string to iterate over it
#   variable even_counter to count all the elements

#3. even_counter variable to counta all positive elements
#   for loop to iterate each element and cast it to string and the replace it in the same list
#   once we have our new string list
#   iterate throught the new list and do a conditional statement
#   if the length of this element % 2 == 0 then count += 1
#   return even_counter

#4. Coding!