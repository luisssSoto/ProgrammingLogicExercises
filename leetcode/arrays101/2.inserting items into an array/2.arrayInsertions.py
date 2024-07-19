"""Array Insertions"""

numbers = [i for i in range(3)]
print(numbers)

'''1. Inserting at the end of an array'''
'''a'''
numbers.append(10)
print(numbers)

'''b'''
numbers += [9]

'''2. Inserting at the start of an array'''
numbers.insert(0, 20)
print(numbers)
    
'''3. Inserting Anywhere in the Array'''
numbers.insert(2, 'any value')
print(numbers)
print()

'''All methods above it are only for python but we need to understand
how we can do it tradionatly:'''

'''1. insert at the end'''
numbers_list = [i for i in range(1, 11)]
print(numbers_list)

'''a) first we need to create any other element at the begining of the array'''
numbers_list.insert(0, 'Zero')
print(numbers_list)

'''b) then we need to move all the elements one place towards to left'''
for i in range(1, len(numbers_list)):
    numbers_list[i - 1] = numbers_list[i]
print(numbers_list)

'''c) now we have enough space to add it at the end'''
numbers_list[10] = 11
print(numbers_list)
print()


'''2. insert at the start of an array'''
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

'''a) add one element at the end of an array'''
even_numbers.append(10)
print(even_numbers)

'''b) shifting all the elements to the right one place'''
for j in range(len(even_numbers) - 1, 0, -1):
    even_numbers[j] = even_numbers[j - 1]
print(even_numbers)

'''c) insert the element at the start'''
even_numbers[0] = -2
print(even_numbers)
print()

'''3. inserting anywhere in the array'''
odd_numbers = [x for x in range(10) if x % 2 != 0]
print(odd_numbers)

'''a) add an element at the end of the array'''
odd_numbers[len(odd_numbers) - 1] = 11
print(odd_numbers)

'''b) shifting all the elements since the specific element to the right (third place)'''
for k in range(len(odd_numbers) - 1, 2, -1):
    odd_numbers[k] = odd_numbers[k - 1]
print(odd_numbers)

'''c now the space fifth we can replace it for any value we want'''
odd_numbers[2] = 'five'
print(odd_numbers)