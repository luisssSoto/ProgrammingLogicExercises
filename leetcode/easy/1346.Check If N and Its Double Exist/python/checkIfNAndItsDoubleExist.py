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

# Approach 1: Sort and look up
def check_if_exist(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    for i in range(len(arr)- 1):
        double = arr[i] * 2
        half = arr[i] / 2
        for j in range(i + 1, len(arr)):
            if arr[j] == double or arr[j] == half:
                 return True
    return False

# Testing
data_test0 = [10,2,5,3]
data_test1 = [3,1,7,11]
data_test2 = [-10,12,-20,-8,15]
print(check_if_exist(data_test2))  

'''Complexity Analysis
Time Complexity: O(n 4)
Space Complexity: O(1)
'''


# Approach 1: Brute Force
def check_if_exist(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j] * 2:
                return True
    return False

'''Complexity Analysis:
 Time complexity: O(n 2)
 Space complexity: O(1)'''

# Approach 3: Set Lookup
def check_if_exist(arr):
    s = set()
    for num in arr:
        if num * 2 in s or num / 2 in s:
            return True
        s.add(num)
    return False


print(check_if_exist(data_test0))

'''Complexity Analysis:
Time complexity: O(n)
Space complexity: O(n)'''

# Approach 4: Sorting and Binary Search
def check_if_exist(arr):
    arr.sort()
    def binary_search(target, array):
        left_pointer = 0
        right_pointer = len(array) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            guess = array[middle_pointer]
            if guess == target:
                return middle_pointer
            elif guess > target:
                right_pointer = middle_pointer
                right_pointer -= 1
            else:
                left_pointer = middle_pointer
                left_pointer += 1
        return -1
    for i in range(len(arr)):
        index = binary_search(arr[i] * 2, arr)
        if index >= 0 and index != i:
            return True
    return False
                

# Testing 
data_test0 = [10,2,5,3]
print(check_if_exist(data_test0))

'''Complexity Analysis:
Time complexity: O(nlogn)
Space complexity: O(n) or O(logn)
The space taken by the sorting algorithm depends on the language of implementation:
Space complexity: O(n) or O(logn)
In Python, the sort() method sorts a list using the Timsort 
algorithm which is a combination of Merge Sort and Insertion 
Sort and has a space complexity of O(n).'''