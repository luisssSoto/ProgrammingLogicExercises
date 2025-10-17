"""Valid Palindrome"""

def is_palindrome(s: str) -> bool:
        start_pointer, last_pointer = 0, len(s) - 1
        while start_pointer < last_pointer:
            while start_pointer < last_pointer and s[start_pointer].isalnum() is False:
                start_pointer += 1
            while start_pointer < last_pointer and s[last_pointer].isalnum() is False:
                last_pointer -= 1
            if s[start_pointer].lower() != s[last_pointer].lower():
                return False
            start_pointer += 1
            last_pointer -= 1
        return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''