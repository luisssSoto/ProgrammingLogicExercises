def designer_pdf_viewer(h, word):
    greatest_high = 0
    for ch in word:
        letter_val = h[ord(ch) - 71 - len(h)]
        if letter_val > greatest_high:
            greatest_high = letter_val
    return greatest_high * len(word)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''