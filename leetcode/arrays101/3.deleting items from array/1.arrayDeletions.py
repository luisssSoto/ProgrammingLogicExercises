"""Deleting from the end of the array"""

class MyArray:
    def __init__(self):
        # Declare an integer array of 10 elements.
        self.__list = [0 for x in range(10)]
        # The array currently contains 0 elements
        self.__length = 0
    def adding_elements(self, value):
        if self.__length <= 10:
            self.__list[self.__length] = value
            self.__length += 1
    def deleting_last_element(self):
        self.__length -= 1
    def getting_length(self):
        return self.__length
    def getting_array(self):
        return self.__list

array1 = MyArray()
# Add elements at the first 6 indexes of the Array.
for i in range(5):
    array1.adding_elements(i)

for j in range(array1.getting_length()):
    print("Index:", j, ":", array1.getting_array()[j])
print()
  
# Adding the other elements
try:
    for k in range(array1.getting_length(), 11):
        array1.adding_elements(k)
except IndexError as e:
    print(e)

for j in range(array1.getting_length()):
    print("Index:", j, ":", array1.getting_array()[j])
print()

# Deletion from the end is as simple as reducing the length
# of the array by 1.
array1.deleting_last_element()
for l in range(array1.getting_length()):
    print(f'Index: {array1.getting_array()[l]}')
print()

# Yup, that's it! Even though we call it a deletion, it's not 
# like we actually freed up the space for a new element, right? 
# This is because we don't actually need to free up any space. 
# Simply overwriting the value at a certain index deletes the 
# element at that index. 

array1.adding_elements(20)
for l in range(array1.getting_length()):
    print(f'Index: {array1.getting_array()[l]}')
print()

"""Deleting from the start of the array"""
# Starting at index 1, we shift each element one positionbto the left.
for i in range(array1.getting_length()-1):
    array1.getting_array()[i] = array1.getting_array()[i+1]
    
for l in range(array1.getting_length()):
    print(f'Index: {array1.getting_array()[l]}')
print()

# Note that it's important to reduce the length of the array by 1.
# Otherwise, we'll lose consistency of the size. This length
# variable is the only thing controlling where new elements might
# get added.
array1.deleting_last_element()

"""Deleting from anywhere in the array"""
# Say we want to delete the element at index 1
for i in range(1, array1.getting_length()-1):
    array1.getting_array()[i] = array1.getting_array()[i+1]

for l in range(array1.getting_length()):
    print(f'Index: {array1.getting_array()[l]}')
print()

# Again, the length needs to be consistent with the current
# state of the array.
array1.deleting_last_element()
