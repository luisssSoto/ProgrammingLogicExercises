"""Check If N And Its Double Exist"""
def checkIfExist(arr):
    for i in range(len(arr)):
            if arr[i] * 2 in arr[i + 1:] or arr[i] * 2 in arr[:i]: return True
    return False

test1 = [10, 2, 5, 3]
test2 = [3,1,7,11]
test3 = [-2,0,10,-19,4,6,-8]
test4 = [0, 0]
test5 = [-20,8,-6,-14,0,-19,14,4]
print(checkIfExist(test5))
print(-2*2)
print(-14 * 2)
#1. input: integers array
#   output: boolean if satisfy next condition: arr[i] == 2 * arr[j]

#2. try to multiply each value
#   if the result is inside the array it is true

#3. iterate through the array
#   multiply that value
#   conditional statement if that value is inside the array returns true
#   

#4. I'm not really sure how the problem is asking