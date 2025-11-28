"""Beatiful Days"""

def beautiful_days(i, j, k):
    count = 0
    for num in range(i, j + 1):
        new_num = int(str(num)[::-1])
        if not abs(num - new_num) % k:
            count += 1
    return count

'''Complexity Analysis:
Time Complexity: O(M * N)
Space Complexity: O(1)'''