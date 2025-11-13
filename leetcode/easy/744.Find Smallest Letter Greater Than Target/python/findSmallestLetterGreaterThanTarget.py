"""744. Find Smallest Letter Greater Than Target"""

def next_greater_letter(letters: list[str], target: str) -> str:
        for ch in letters:
            if ord(ch) > ord(target):
                return ch
        return letters[0]
        
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def next_greater_letter(letters: list[str], target: str) -> str:
    left = 0
    right = len(letters) - 1
    greater = ""
    while left <= right:
        middle = (left + right) // 2
        if letters[middle] > target:
            greater = letters[middle]
            right = middle - 1
        else:
            left = middle + 1
    if greater:
        return greater
    else:
        return letters[0]

'''Complexity Analysis:
Time Complexity: O(log N)
Space Complexity: O(1)'''