"""Arrays"""

'''Generally arrays are good to randomly Read an element but not to 
inserting or deleting elements'''
class MyArray:
    def __init__(self, size):
        self.__array = [0 for i in range(size)]
    def get_array(self):
        return self.__array
    def read_element(self, index):
        try:
            return self.__array[index]
        except IndexError: 
            return f'Sorry but the index is out of the range the len of the array is: {len(self.__array)}'
    def delete_element(self, index):
        for i in range(index, len(self.__array) - 1):
            self.__array[i] = self.__array[i + 1]
    def insert_element(self, index, element):
        self.delete_element(index)
        self.__array[index] = element         

my_array1 = MyArray(5)
print(len(my_array1.get_array()))
print(my_array1.get_array())
print()

'''Read O(1)'''
print(my_array1.read_element(1))

'''Insert O(n)'''
my_array1.insert_element(0, 10)
print(my_array1.get_array())
my_array1.insert_element(3, 20)
print(my_array1.get_array())

'''Delete O(n)'''
my_array1.delete_element(2)
print(my_array1.get_array())
my_array1.insert_element(4, 50)
print(my_array1.get_array())
my_array1.delete_element(4)
print(my_array1.get_array())


