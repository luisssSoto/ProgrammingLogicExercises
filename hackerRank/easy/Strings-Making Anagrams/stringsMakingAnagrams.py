"""Strings Making Anagrams"""
def make_anagram(a, b):
    # Write your code here
    count_del = 0
    dict_a, dict_b = {}, {}
    
    for letter in a:
        if letter not in dict_a:
            dict_a[letter] = 1
        else:
            dict_a[letter] += 1
    for letter in b:
        if letter not in dict_b:
            dict_b[letter] = 1
        else:
            dict_b[letter] += 1
    
    for key in dict_a:
        if key not in dict_b:
            count_del += dict_a[key]
        else:
            count_del += abs(dict_a[key]-dict_b[key])
    for key in dict_b:
        if key not in dict_a:
            count_del += dict_b[key]
    return count_del
    
    '''1.
    input: two strings
    output: integer
    
    2.
    count to count all deletions
    dictionary for both strings
    iterate for each dictionary
    if element in other dictionary
        keep the difference
    else:
        count_to count += dictionary[element]
    
    3.
    count_del = 0
    for letter in string1:
        if letter not in string1:
            dict1[letter] = 1
        else:
            dict1[letter] += 1
    for key in dict1:
        if key not in dict2:
            count_del += dict1[key]
        else:
            count_del += abs(dict1[key]-dict2[key])
    return count_del
    
    4. happy coding
    '''