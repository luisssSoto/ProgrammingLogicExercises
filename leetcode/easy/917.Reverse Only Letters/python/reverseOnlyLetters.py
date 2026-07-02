# 917. Reverse Only Letters

def reverse_only_letters(s: str) -> str:
    array_s = [character for character in s]
    n = len(array_s)
    left = 0
    right = n - 1
    while left < right:
        if array_s[left].isalpha() is True:
            while array_s[right].isalpha() is False:
                right -= 1
            array_s[left], array_s[right] = array_s[right], array_s[left]
            right -= 1
        left += 1
    return "".join(array_s)

# Testcase
s1 = "ab-cd"
s2 = "Test1ng-Leet=code-Q!"
s3 = "a-bC-dEf-ghIj"
print(reverse_only_letters(s3))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''