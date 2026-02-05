"""Modified Kaprekar Numbers"""

def kaprekarNumbers(p: int, q: int):
    found = False
    for num in range(p, q + 1):
        sq = str(num ** 2)
        mid = len(sq) // 2
        left = int(sq[:mid]) if sq[:mid] else 0
        right = int(sq[mid:])
        if left + right == num:
            print(num, end=" ")
            found = True
    if not found:
        print('INVALID RANGE')

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''