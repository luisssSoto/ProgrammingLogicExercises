# Check if the Sentence Is Pangram

def check_if_pangram(sentence: str) -> bool:
    alphabet = ord('z') - ord('a') + 1
    unique_chrs = set(sentence)
    if len(unique_chrs) == alphabet:
        return True
    else:
        return False

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''