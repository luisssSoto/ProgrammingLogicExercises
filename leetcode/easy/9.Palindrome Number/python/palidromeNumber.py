"""Palindrome Number"""

# My Approach: Cast to String and Two Technique Pointer
def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left_pointer = 0
        right_pointer = len(x) - 1
        while left_pointer < right_pointer:
            if x[left_pointer] != x[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''