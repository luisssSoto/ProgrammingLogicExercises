"""Number Of Lines To Write String"""

def number_of_lines(s: str, widths: list[int])-> list[int]:
    count_rows, count_width = 1, 0
    for ch in s:
        count_width += widths[ord(ch) - ord('a')]
        if count_width > 100:
            count_rows += 1
            count_width = widths[ord(ch) - ord('a')]
    return [count_rows, count_width]

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def number_of_lines(widths: list[int], s: str) -> list[int]:
        alphabet = [chr(letter) for letter in range(97, 123)]
        pixels_dict = {letter: pixel for letter, pixel in zip(alphabet, widths)}
        count, count_row = 0, 1
        for i in range(len(s)):
            count += pixels_dict[s[i]]
            if count > 100:
                count = pixels_dict[s[i]]
                count_row += 1
        return [count_row, count]

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''