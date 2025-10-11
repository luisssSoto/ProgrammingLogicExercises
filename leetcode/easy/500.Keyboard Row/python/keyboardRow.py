"""Keyboard Row"""

def keyboard_row(words: list[str])-> list[str]:
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    keyboard_words = []
    for word in words:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        keyboard_words = []
        for word in words:
            is_available = True
            if word[0].lower() in row1:
                for letter in word:
                    if letter.lower() not in row1:
                        is_available = False
                        break
            elif word[0].lower() in row2:
                for letter in word:
                    if letter.lower() not in row2:
                        is_available = False
                        break
            elif word[0].lower() in row3:
                for letter in word:
                    if letter.lower() not in row3:
                        is_available = False
                        break
            if is_available is True:
                keyboard_words.append(word)
        return keyboard_words

# Testcase
words1 = ["Hello","Alaska","Dad","Peace"]
print(keyboard_row(words1))


'''Complexity Analysis:
Time Complexity: O(N * M)
Space Complexity: O(1)'''

