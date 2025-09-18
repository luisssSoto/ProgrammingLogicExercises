"""Lucky Seven"""
# cook your dish here
s = input()
for index, letter in enumerate(s):
    if index == 6:
        print(letter)
        break