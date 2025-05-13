"""Valid Mountain Array"""
# My Approach
def valid_mountain_array(arr):
    if len(arr) < 3:
        return False
    greater_number = max(arr)
    index_greater_number = arr.index(greater_number)
    increased_validations = index_greater_number
    decreased_validation = len(arr) - 1 - index_greater_number
    if decreased_validation == 0 or increased_validations == 0:
        return False
    count_increased = count_decreased = 0
    for j in range(len(arr) - 1):
        if arr[j] < arr[j + 1] and j < index_greater_number:
            count_increased += 1
        elif arr[j] > arr[j + 1] and j >= index_greater_number:
            count_decreased += 1
        else:
            return False
    if count_increased == increased_validations and count_decreased == decreased_validation:
        return True

test1 =  [0,1,2,3,4,5,6,7,8,9]
print(valid_mountain_array(test1))
l = test1[:]
print(l)
m = max(l)
print(m)
print(l.index(m))
#1. input: integers array
#   output: boolean according if the integer nums strictly increase and then decrease

#2. edge cases: if the length it's >= 3 
#   iterate the array
#   conditional statement if numbers are increasing and after decreasing

# 3. if lenght arr >= 3: then return False
#     for loop know what is the index of the element greater
#     for loop each element range
#     if arr[i] < arr[i + 1] and i < greater: continue
#     elif arr[i] > arr[i + 1] and i >= than greater: continue
#     else return False
#     if all the tests pass so now return True

# 4. coding you can find the greater with max function 

# Approach 1: One Pass
def valid_mountain_array(arr):
    i = 0
    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        i += 1
    if i == 0 or i == len(arr) -1:
        return False
    while i + 1 < len(arr) and arr[i] > arr[i + 1]:
        i += 1
    return i == len(arr) - 1

# Testing 
dataTest0 = [2,1]
dataTest1 = [3,5,5]
dataTest2 = [0,3,2,1]
dataTest3 = [0,2,3,4,5,2,1,0]
dataTest4 = [0,2,3,4,5,2]
dataTest5 = [9,8,7,6,5,4,3,2,1,0]
dataTest6 = [2,1,2,3,5,7,9,10,12,14,15,16,18,14,13]

print(valid_mountain_array(dataTest6))

'''Complexity Analysis

Time Complexity: O(N), where N is the length of A.

Space Complexity: O(1).'''