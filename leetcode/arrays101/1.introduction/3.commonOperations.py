"""Common Operations in Array"""

even_list = [x if x % 2 == 0 else 'odd' for x in range(11)]
print(even_list)

'''writing'''
even_list[0] = 'zero'
print(even_list)

'''reading'''
print(even_list[0])

'''for loop writing range() function generator'''
for i in range(5):
    print(even_list[i], end=' ')
print()

'''for loop without range()'''
for element in even_list:
    print(element, end=' ')