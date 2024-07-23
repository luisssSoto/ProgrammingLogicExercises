"""Replace Elements with Greatest Element on Right Side"""
def replace_elements(arr):
    high = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        temp = arr[i]
        arr[i] = high
        high = max(high, temp)
    arr[-1] = -1
    return arr

#This method exceeds runtime
def replace_elements(arr):
    #edge cases
    if len(arr) == 1:
        arr[0] = -1
        return arr
    for i in range(len(arr) - 1):
        arr[i] = max(arr[i + 1 :])
    arr[-1] = -1
    return arr


test1 = [57010,40840,69871,14425,70605]
test2 = [17,18,5,4,6,1]
test3 = [400]
test4 = ''
print(replace_elements(test1))
'''
1. input: integer array
    output: integer array: modified by exchanging the greatest element
    its right but the last one must be 0
2. edge cases: length ==1 return the array [-1]
    iterate the array
    conditional statement for each element
    knowing where is the greatest element its right
    replace it with that value
3. if len(arr) == 0: arr[0] = -1
    greatest = arr[-1]
    for i in range(len(arr)):
    if i == len(arr) - 1:
    arr[i] = -1
    for j in range(1, len(arr) - 1):
    if arr[j] > greatest:
    greatest = arr[j]
    end of the second loop
    arr[i] = greatest 
    end of the first loop
4. coding carefully

    
    
'''