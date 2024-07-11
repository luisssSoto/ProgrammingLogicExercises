"""Ransom Note"""
def ransom_note(ransomNote, magazine):
    are_same_characters = False
    ransom_note_dict = {}
    magazine_dict = {}
    if len(ransomNote) > len(magazine):
       return are_same_characters
    else:
        for element in ransomNote:
            if element not in ransom_note_dict:
                ransom_note_dict[element] = 1
            else:
                ransom_note_dict[element] += 1
        for element in magazine:
            if element not in magazine_dict:
                magazine_dict[element] = 1
            else:
                magazine_dict[element] += 1
    print(ransom_note_dict, magazine_dict)
    keys = len(ransom_note_dict)
    matches = 0
    for key, value in ransom_note_dict.items():
        if key in magazine_dict:
            if value <= magazine_dict[key]:
                print(value, '=', magazine_dict[key])
                matches += 1
                if keys == matches:
                    are_same_characters = True
                    return are_same_characters
            else:
                return are_same_characters
        else:
            return are_same_characters
        
      
test1 = "bg"
test2 = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(ransom_note(test1, test2))

print(test1.count('u'))
def ransom_note(ransomNote, magazine):
    isTrue = False
    if len(ransomNote) > len(magazine):
        return isTrue
    else:
        for element in ransomNote:
            if ransomNote.count(element) <= magazine.count(element):
                isTrue = True
            else:
                isTrue = False
                return isTrue
        return isTrue
    
test1 = "bg"
test2 = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(ransom_note(test1, test2))

#1. input: two strings
#   output: boolean

#2. iterate the ransomNote
#   doing a dictionary of both ransomNote and magazine
#   compare the same amount of letters

#3. if length of magazine is less than ransomNote return False
#   else continue with all the proccess
#   iterate each argument with foor loop
#   create a dictionary with the data of each argument
#   if the letter in argument, then add it + 1
#   else create the new key plus 1
#   once all the dicts are ready, iterate for ransomNote
#   if element in magazine continue else return False
#   if each value has the same amount of letters return True
#   else break and return False

#4. Practice the dictionary, coding