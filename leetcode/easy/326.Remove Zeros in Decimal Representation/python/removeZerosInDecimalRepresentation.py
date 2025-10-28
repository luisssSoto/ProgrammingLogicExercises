"""Remove Zeros in Decimal Representation"""

# Approach 1:
def remove_zeros(n: int) -> int:
    n = str(n)
    n = n.replace("0", "")
    return int(n)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Approach 2:
def remove_zeros(n: int) -> int:
    str_n = ""
    while n > 0:
        remain = n % 10
        if remain != 0:
            str_n += str(remain)
        n //= 10
    n = str_n[::-1]
    return int(n)

'''Complexity Analysis:
Time Complexity: O(Log(N))
Space Complexity: O(Log(N))'''