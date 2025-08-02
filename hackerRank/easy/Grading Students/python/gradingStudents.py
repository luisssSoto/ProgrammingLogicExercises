"""Grading Students"""

def grading_students(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        next_mul_5 = grades[i] // 5 * 5 + 5
        difference = next_mul_5 - grades[i]
        if difference < 3:
            grades[i] = next_mul_5
    return grades

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''