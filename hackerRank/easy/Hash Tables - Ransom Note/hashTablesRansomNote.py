"""Hash Tables: Ransom Note"""
def check_magazine(magazine, note):
    is_it_possible = 'Yes'
    # create magazine dict
    magazine_dict = {}
    for word in magazine:
        if word not in magazine_dict:
            magazine_dict[word] = 1
        else:
            magazine_dict[word] += 1
    #create note_dict
    note_dict = {}
    for word in note:
        if word not in note_dict:
            note_dict[word] = 1
        else:
            note_dict[word] += 1
    # iterate note_dict to match all the occurrences
    for key in note_dict:
        if key not in magazine_dict:
            is_it_possible = 'No'
        elif magazine_dict[key] < note_dict[key]:
            is_it_possible = 'No'
    print(is_it_possible)

magazine = "ive got a lovely bunch of coconuts"
magazine_list = magazine.split()
print(magazine_list) 

note = "ive got some coconuts"
note_list = note.split()
print(note_list)

print(check_magazine(magazine_list, note_list))

'''
1.
input: two strings array 
output: one string 'yes' if there are the same or more amount of words
in the magazine compare with note

2. 
edge cases: nothing so far
key structure: dictionary
compare the value of both dictionaries

3. 
figure out how to convert string to dictionary
old method
a) iterate note dictionary:
b) conditional statement if the element note in magazine dictionary
b1) if so... conditional statement to know if the same or more amount value
    if not return variable 'No'
b2) if not return variable 'No'
c) return variable 'Yes'

4.Happy coding


'''
