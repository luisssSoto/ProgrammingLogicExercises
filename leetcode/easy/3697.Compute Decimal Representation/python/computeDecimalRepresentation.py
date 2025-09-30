"""Compute Decimal Representation"""

def decimal_representation(n: int) -> list[int]:
    dec = 1
    result = []
    while n > 0:
        dec *= 10
        remain = n % dec
        coc = n // dec
        n = coc * dec
        if remain != 0:
            result.append(remain)
    return result[::-1]
    

'''Complexity Analysis:
Time Complexity: O(Log10(N))
Space Complexity: O(Log10(N))'''