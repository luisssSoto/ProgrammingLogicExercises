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
'''a) first we need to create a class that works like a limited list'''
class CapacityError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        
class LimitedArray:
    def __init__(self):
        self.__array = [0 for x in range(6)]
        self.__length = 0
        
    def insert_element(self, element, place):
        if place < len(self.__array):
            self.__array[place] = element
            self.__length += 1
        else: raise CapacityError
    
    def get_array(self):
        return self.__array
    
'''In the case there is enough space is easy:'''
limited_array1 = LimitedArray()

# inserting elements
for i in range(3):
    limited_array1.insert_element(i, limited_array1._LimitedArray__length)

# print each element
for j in range(len(limited_array1.get_array())):
    print(f"Index {j} contains {limited_array1.get_array()[j]}")

# print the whole array
print(limited_array1.get_array())

# inserting another element
limited_array1.insert_element(10, limited_array1._LimitedArray__length)
print(limited_array1.get_array())

'''But case there isn't enough space is more difficult:'''

'''a) I need to fill the empty spaces..'''
for k in range(4, 6):
    limited_array1.insert_element('no empty', k)
print(limited_array1.get_array())

'''b) then we need to move all the elements one place towards to left'''
for l in range(len(limited_array1.get_array())-1):
    limited_array1.get_array()[l] = limited_array1.get_array()[l+1]
print(limited_array1.get_array())

'''c) now we have enough space to add it at the end'''
limited_array1.get_array()[5] = 'full'
print(limited_array1.get_array())
print()

'''2. insert at the start of an array'''

'''a) shifting all the elements to the right one place'''
for m in range(len(limited_array1.get_array())-1, 0, -1):
    limited_array1.get_array()[m] = limited_array1.get_array()[m-1]

print(limited_array1.get_array())

'''c) insert the element at the start'''
limited_array1.get_array()[0] = "first element"
print(limited_array1.get_array())
print()

'''3. inserting anywhere in the array'''

'''a) shifting all the elements since the specific element to the right (third place)'''
for n in range(len(limited_array1.get_array())-1, 1, -1):
    limited_array1.get_array()[n] = limited_array1.get_array()[n-1]
print(limited_array1.get_array())

'''c now the space third we can replace it for any value we want'''
limited_array1.get_array()[2] = "third space"
print(limited_array1.get_array())
print()