"""Duplicate Zeros"""
# Approach 1
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

# Approach 2
def duplicate_zeros(arr):
    i = 0
    while i <= len(arr) - 1:
        if arr[i] ==  0:
            for j in range(len(arr) - 1, i, -1):
                arr[j] = arr[j - 1]
            i += 1
        i += 1
    return arr

test1 = [0,1,7,6,0,2,0,7]
print(duplicate_zeros(test1))

# Approach 3
def duplicate_zeros(arr):
    possible_dups = 0
    length_ = len(arr) - 1

    # Find the number of zeros to be duplicated
    for left in range(length_ + 1):

        # Stop when left points beyond the last element in the original list
        # which would be part of the modified list
        if left > length_ - possible_dups:
            break

            # Count the zeros
        if arr[left] == 0:
            # Edge case: This zero can't be duplicated. We have no more space,
            # as left is pointing to the last element which could be included  
            if left == length_ - possible_dups:
                arr[length_] = 0 # For this zero we just copy it without duplication.
                length_ -= 1
                break
            possible_dups += 1

    # Start backwards from the last element which would be part of new list.
    last = length_ - possible_dups

    # Copy zero twice, and non zero once.
    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + possible_dups] = 0
            possible_dups -= 1
            arr[i + possible_dups] = 0
        else:
            arr[i + possible_dups] = arr[i]
    return arr
            

test1 = [0,1,7,6,0,2,0,7]
print(duplicate_zeros(test1))
