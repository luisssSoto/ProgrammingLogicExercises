"""In-place array operations introduction"""
'''in-place array operations reduces the space complexity,
so you can try it wherever you can'''

'''Try this exercise whit different approaches:
Given an Array of integers, return an Array where every 
element at an even-indexed position is squared.'''

l1 = [9, -2, -9, 11, 56, -12, -3]
print(l1)

'''1. bad approach because increases the space complexity'''
l2 = l1[:]
for number in l1:
    if l1.index(number) % 2 == 0:
        i = l1.index(number)
        number = number * number
        l2[i] = number
print(l2)

'''2. good approach because we work with the same array'''
for i in range(0,len(l1),2):
    l1[i] = l1[i] * l1[i]
print(l1)
