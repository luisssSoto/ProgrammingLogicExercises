"""Binary Search"""
'''O(Log n) Logarithmmic time'''

# 1. initialize three vars (lowest_index, highest_index, middle_index)
# 1. lowest_index = 0, highest_index = arr.len - 1
# 2. while lowest_index <= highest_index
# 3. middle_index = (lowest_index + highest_index) // 2 
# 4. if arr[middle_index] equal to item
# 4.1 if so.... return the middle_index
# 4.2 else if arr[middle_index] > item
# 4.3 if so... highest_index = middle_index -1
# 4.4 else if arr[middle_index] < item
# 4.5 if so... lowest_index = middle_index + 1
# 5. return None
def binary_search(array, item):
    lowest_index = 0
    highest_index = len(array) - 1
    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        guess = array[middle_index]
        if guess == item:
            return middle_index
        elif guess > item:
            highest_index = middle_index -1
        elif guess < item:
            lowest_index = middle_index + 1
    return None

a = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(a, 4))

