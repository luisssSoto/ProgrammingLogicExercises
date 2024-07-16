"""array deletions"""

'''1. deleting from the end of an array'''
even_list = [x for x in range(10) if x % 2 == 0]
print(even_list)

del even_list[-1]
print(even_list)

even_list.pop()
print(even_list)
print()

'''2. Deleting from the Start of an Array'''
del even_list[0]
print(even_list)
print()

'''3. Deleting from Anywhere of an Array'''
del even_list[1]
print(even_list)