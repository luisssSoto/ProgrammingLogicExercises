"""Angry Professor"""

def angry_professor(k: int, a: list[int]) -> str:
    result = "YES"
    students_on_time = 0
    for time in a:
        if time < 1:
            students_on_time += 1
        if students_on_time == k:
            result = "NO"
            break
    return result

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''