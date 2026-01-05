"""Append and Delete"""
def append_and_delete(s, t, k):
    common = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common += 1
        else:
            break
    min_operations = len(s) - common + len(t) - common
    if k >= len(s) + len(t):
        return 'Yes'
    if k >= min_operations and (k - min_operations) % 2 == 0:
        return 'Yes'
    return 'No'

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# testcase 1.
s1 = "y"
t1 = "yu"
k1 = 2
s2 = "aba"
t2 = "aba"
k2 = 3
print(append_and_delete(s2, t2, k2))