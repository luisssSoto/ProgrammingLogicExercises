"""Squares of a Sorted Array"""
def sorted_squares(nums):
    sort_list = list(map(lambda x: x * x, nums))
    sort_list.sort()
    return sort_list

test1 = [-4,-1,0,3,10]
print('t', sorted_squares(test1))

test1 = [16,1,0,9,100]
is_sort = False

while is_sort == False:
    is_sort = True
    for i in range(len(test1)-1):
        if test1[i] > test1[i + 1]:
            test1[i], test1[i + 1] = test1[i + 1], test1[i]
            is_sort = False
    print(test1)


#1. input: non-decreasing list
#   output: non-decreasing list of squares numbers

#2. iterate the nums list
#   square it and assing the new list
#   sort the new list

#3. square_list will be the new square numbers list
#   iterate for the nums list
#   square each element and append it to the new list
#   then order the new list
#   iterate for the list with a while loop
#   create a less_value and assign the firs element of the new list
#   while isSort variable is False continue
#   for loop the new_list 
#   conditional statement if this element < less_value then
#   less_value = thisElement
#   newList[less_value[i]], thisElement = thisElement

#4. sort the list with the well-known method sort
