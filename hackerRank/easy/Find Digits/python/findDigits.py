"""Find Digits"""

def find_digits(n: int) -> int:
    numbers = [int(x) for x in str(n)]
    count = 0
    for num in numbers:
        if num == 0:
            continue
        elif n % num == 0:
            count += 1
    return count

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

def find_digits(n: int) -> int:
    temp = n
    count = 0
    while temp > 0:
        digit = temp % 10
        if digit != 0 and n % digit == 0:
            count += 1
        temp //= 10
    return count

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

print(find_digits(1012))