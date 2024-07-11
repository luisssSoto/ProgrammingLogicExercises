"""Duplicate Zeros"""
def duplicate_zeros(arr):
    zero_match = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_match += 1
            if zero_match == 1:
                arr.insert(i + 1, 0)
                arr.pop()
            elif zero_match == 2:
                zero_match = 0
    print(arr)

test1 = [0,1,7,6,0,2,0,7]
duplicate_zeros(test1)
#1. input: array
#   output: nothing only modify the same array, which has the same length but with twice 0

#2. iterate the array with length of the array
#   conditional if the element is equal 0
#   if so duplicate it and put it next to the right the first one

#3. iterate the array range(len(arr))
#   conditional statement if the element is equal to 0
#   if so, use insert function next right it and delete the last one
#   nothing returns

#4. all it's fine just coding now!

l = [x for x in range(5)]
print(l)
l.pop()
print(l)