"""Alternating Characters"""
def alternating_characters(s):
    count_del = 0
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            count_del += 1
    return count_del

data1 = 'ABABABAA'
print(alternating_characters(data1))

'''
1. 
input: string
output: integer as a result of all the deletions can be in order to make 
        the string each element adjacent don't match
        
2.
variable to count all deletions
iterate the string
    conditional statement wheter the element is equal to the next one
        if so replace the first one and add by one the count variable

3.
count_del = 0
steps_back = 0
for i in range(steps_back,len(s)-1):
    steps_back += 1
    if s[i] == s[i+1]:
        s = s.replace(s[i], '')
        count_del += 1
        steps_back -= 1
return count_del

4.
happy coding!


'''