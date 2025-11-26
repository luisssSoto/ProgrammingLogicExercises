"""Unique Morse Code Words"""

def unique_morse_representation(words: list[str]) -> int:
        letters = [chr(num) for num in range(97, 123)]          
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_code_words = {letter: code for letter, code in zip(letters, morse_code)}
        uniques = set()
        for word in words:
            code = ""
            for ch in word:
                code += morse_code_words[ch]
            if code not in uniques:
                uniques.add(code)
        return len(uniques)

'''Complexity Analysis:
Time Complexity: O(N * K)
Space Complexity: O(N * K)'''