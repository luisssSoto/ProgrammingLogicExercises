"""Sorting Buble Sort"""
def count_swaps(a):
    is_it_sorted = False
    count_swap = 0
    while is_it_sorted == False:
        is_it_sorted = True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                is_it_sorted = False
                count_swap += 1
    print(f'Array is sorted in {count_swap} swaps')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

data1 = [6,4,1]
count_swaps(data1)

'''
1.
input: integer array
output: integer as a result of count all the swaps in order
to sort the array in ascending order with a burble approach

2. 
edge case: is it sort True then return 0 and the first and last element
key: for loop and while
a) create a condition in order to control 
b) while is_it_sort:
b) change the value is_it_sort = True
c) for i in range(len)
d) conditional statement if the first element is < than the i+
c) then swap it 
d) count_swap += 1
e) is_it_sort = False
'''