"""Search in array"""
'''Linear search is an algorithm that is common use in order to look for one element,
it's quite slow if we compare it with the binary search, this is another algorithm,
which is faster if you're going look more than one element and if the list is sorted,
but first we can take a look about linear search'''

'''actually we can do a function'''
def linear_search(element, array):
    # handle the edge cases
    if len(array) == 0:
        return False
    for character in array:
        if isinstance(character, int) == False:
            return False
    for number in array:
        if number == element:
            return True
    return False

test1 = [x for x in range(1, 11)]
print(test1)
print(linear_search(11,test1))

'''2. approach'''
element = 2
for i in range(len(test1)):
    if test1[i] == element:
        print(True)
        
'''3. approach'''
str_list = ['hello' if x % 2 == 0 else 'hola' for x in range(10)]
print(str_list)
print(str_list.index('hello', 2))

