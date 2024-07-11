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
