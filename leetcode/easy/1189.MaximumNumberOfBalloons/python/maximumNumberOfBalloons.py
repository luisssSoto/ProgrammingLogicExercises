# 1189.Maximum Number Of Balloons
def maxNumberOfBalloons(self, text: str) -> int:
    freq_letters = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
    for letter in text:
        if letter in freq_letters:
            freq_letters[letter] += 1
    res = freq_letters['b']
    for key in freq_letters:
        dividend = 1
        if key == 'l' or key == 'o':
            dividend = 2
        val = freq_letters[key] // dividend
        if val < res:
            res = val
    return res

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''