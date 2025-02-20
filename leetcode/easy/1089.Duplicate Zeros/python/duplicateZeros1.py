"""Duplicate Zeros"""
'''Time complexity increase a lot but its in-place'''
def duplicate_zeros(arr):
    step = 0
    for i in range(step, len(arr)-1):
        if arr[step] == 0:
            for j in range(len(arr)-1, step, -1):
                arr[j] = arr[j-1]
            step += 2
        else:
            step += 1
        if step >= len(arr)-1:
            return arr

data = [0,1,7,6,0,2,0,7]
data1 = [1,0,2,3,0,4,5,0]
data2 = [1,2,3]
data3 = [1,5,2,0,6,8,0,6,0]
print(duplicate_zeros(data3))

'''
1.
input: integer array
output: modified integer array which all occurrences of zero copy by one
        and all the data shift to right

2.
iterate array
look up all zeros
if there is a zero shift the elements to right one place

3. 
for loop through the array if zero length arr -1
initialize a counter zero in order to step each time it was found
and another for loop to shift to right all elements from back to front

4.happy coding!
'''