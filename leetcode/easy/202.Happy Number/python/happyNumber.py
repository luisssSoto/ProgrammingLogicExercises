"""Happy Number"""

def is_happy(n):
    for _ in range(10):
        n = str(n)
        n = [int(x) ** 2 for x in n]
        n = sum(n)
        if n == 1:
            return True
    return False

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''

def is_happy(n):
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digits = divmod(n, 10)
            total_sum += digits ** 2
        return total_sum
    seen = set()
    while n != 1 and n not in seen:
         seen.add(n)
         n = get_next(n)
    return n == 1

'''Complexity Analysis:
Time Complexity: O(log N)
Space Complexity: O(log N)'''

def is_happy(n):
    for _ in range(10):
        total_sum = 0
        while n != 0:
            n, digits = divmod(n, 10)
            total_sum += digits ** 2
        if total_sum == 1:
            return True
        else:
            n = total_sum
    return False

print(is_happy(2))

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''