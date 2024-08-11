"""Two Strings"""
def two_strings(s1, s2):
    # Write your code here
    is_substring = "NO"
    for character in s1:
        if character in s2:
            is_substring = "YES"
            return is_substring
    return is_substring
    
'''
1.
input: two string
output: string YES or NO, depend whether there is a substring or not

2.
create a variable is_substring = False
iterate s1
    conditional statement if to know it character in s2
        if so set is_substring to True and return it
return is_substring

3.
is_substring = False
for character in s1:
    if character in s2:
        is_substring = True
        return is_substring
return is_substring

4. quite easy
        
'''
