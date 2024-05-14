"""ISB-10 Validation """
def valid_ISBN10(isbn):
    veredict = False
    if len(isbn) == 10 and isbn[:9].isdigit() and (isbn[-1].isdigit() == True or isbn[-1] == 'X'):
        total = 0
        for i in range(len(isbn)):
            if isbn[i].isdigit() == True:
                newValue = int(isbn[i]) * (i + 1)
                total += newValue
            else:
                total += 100
        print(total)
        total %= 11
        if total == 0:
            veredict = True
        else:
            veredict = False
    return veredict

test = '123456789T'
test1 = '634X948251'
print(valid_ISBN10(test1))
print(220 % 11)
print(test1[:9].isdigit() == True)
