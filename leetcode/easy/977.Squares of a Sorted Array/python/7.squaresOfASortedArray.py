"""Squares of a Sorted Array"""
def sorted_squares(nums):
    sort_list = list(map(lambda x: x * x, nums))
    sort_list.sort()
    return sort_list

test1 = [-4,-1,0,3,10]
print('t', sorted_squares(test1))

'''Time Complexity: O(NlogN), where N is the length of A.

Space complexity : O(N) or O(logN)

The space complexity of the sorting algorithm depends on the implementation of each program language.

For instance, the list.sort() function in Python is implemented with the Timsort algorithm whose space complexity is O(N).

In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm whose space complexity is O(logN). However, if the array is highly structured (has few sorted subarrays), then linear space may be used instead.'''



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

'''Approach 2: Two Pointer Technique'''
def sorted_squares(nums):
    insert_pointer = right_pointer = len(nums) - 1
    left_pointer = 0
    sorted_square_array = nums[:]
    for insert_pointer in range(insert_pointer, -1, -1):
        if abs(nums[left_pointer]) < abs(nums[right_pointer]):
            square = nums[right_pointer] ** 2
            right_pointer -= 1
        else:
            square = nums[left_pointer] ** 2
            left_pointer += 1
        sorted_square_array[insert_pointer] = square
    return sorted_square_array

test1 = [-4,-1,0,3,10]
print(sorted_squares(test1))

'''Complexity Analysis:
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N) if you take output into account and O(1) otherwise.'''