"""Height Checker"""
def height_checker(heights):
    #edge cases
    sorted_heights = sorted(heights)
    if sorted_heights == heights:
        return 0
    #normal cases
    else:
        wrong_positions = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                wrong_positions += 1
        return wrong_positions
                    

heights =  [1,1,4,2,1,3]
heights1 = [5,1,2,3,4]
expected = [1,1,1,2,3,4]

print(height_checker(heights))

'''
1.
input: integer array
output: integer number which represents all the indexes that don't match
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
output: 3

2.
edge cases: increasing order return 0
key: it is not neccessary to sort the array only compare it with 
the sorted array and keep track of all the indexes that don't match
with the sorted array

3. 
sort_heights = sort(heights)
conditional statement if sort_heights == to heights if so return 0
else
    for loop in order to iterate each element with the sorted heights
        conditional statement to know if n element is different to its contrapart if so
            then add 1 to the count variable
return the count variable
    
4. coding

'''
def height_checker(heights):
    unorder_heights = heights[:]
    heights.sort()
    count_wrong_student_place = 0
    for i in range(len(heights)):
        if heights[i] != unorder_heights[i]:
            count_wrong_student_place += 1
    return count_wrong_student_place

# Testing 
data_test_0 = [1,1,4,2,1,3]
data_test_1 = [5,1,2,3,4]
data_test_2 = [1,2,3,4,5]
print(height_checker(data_test_2))

'''Complexity Analysis:
 * Time Complexity: O(NlogN)
 * Space Complexity: O(N)'''