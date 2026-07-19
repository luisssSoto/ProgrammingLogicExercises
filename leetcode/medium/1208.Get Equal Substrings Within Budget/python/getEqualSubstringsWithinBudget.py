#1208. Get Equal Substrings Within Budget

def equal_substring(s: str, t: str, maxCost: int) -> int:
    left = right = ans = curr_sum = 0
    for right in range(len(s)):
        curr_sum += abs(ord(t[right]) - ord(s[right]))
        while curr_sum > maxCost:
            curr_sum -= abs(ord(t[left]) - ord(s[left]))
            left += 1
        ans = max(ans, right - left + 1)
    return ans

# Testcases
s1 = "abcd"
t1 = "bcdf"
maxCost1 = 3

s2 = "abcd"
t2 = "cdef"
maxCost2 = 3

s3 = "krrgw"
t3 = "zjxss"
maxCost3 = 19
print(equal_substring(s3, t3, maxCost3))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity : O(1)'''