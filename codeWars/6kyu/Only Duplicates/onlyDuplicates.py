"""Only Duplicates"""
def only_duplicates(st):
    duplicate = st
    duplicate_words = ''
    for word_duplicate in duplicate:
        count = 0
        for word in st:
            if word_duplicate == word:
                count += 1
            if count == 2:
                duplicate_words += word_duplicate
                break
    return duplicate_words

test = "abccdefee"
print(only_duplicates(test))
output = "cceee"

def only_duplicates2(st):
    duplicates = ''
    for element in st:
        without_element = st.replace(element, '', 1)
        if element in without_element:
            duplicates += element
    return duplicates

print(only_duplicates2(test))


"""Cleverest solution by AverageWizard and others"""
def only_duplicates(st):
    return ''.join([x for x in st if st.count(x) > 1])
print(only_duplicates(test))
