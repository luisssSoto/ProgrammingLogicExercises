def print_formatted(number):
    # your code goes here
    limit = number + 1
    spacesD, spacesO, spacesH, spacesB = 0, 0, 0, 0
    countDec, countOct, countHex, countBin = 1, 1, 1, 1

    for decimal in range(1, limit):
        lenDec = len(str(decimal))

        strOct = str(oct(decimal))
        strOct = strOct.replace('0o','')
        strHex = str(hex(decimal))
        strHex = strHex.replace('0x','')
        for h in strHex:
            strHex = strHex.replace(h, h.capitalize())
        strBin = str(bin(decimal))
        strBin = strBin.replace('0b','')

        if lenDec > countDec:
            countDec += 1
            spacesD += 1
        if len(strOct) > countOct:
            countOct += 1
            spacesO += 1
        if len(strHex) > countHex:
            countHex += 1
            spacesH += 1
        if len(strBin) > countBin:
            countBin += 1
            spacesB += 1

        spaceDec = ' ' * (len(str(bin(number)))-2-spacesD-1)
        spaceOct = ' ' * (len(str(bin(number)))-2-spacesO)
        spaceHex = ' ' * (len(str(bin(number)))-2-spacesH)
        spaceBin = ' ' * (len(str(bin(number)))-2-spacesB)
    
        print(f'{spaceDec}{decimal}{spaceOct}{strOct}{spaceHex}{strHex}{spaceBin}{strBin}')

print_formatted(17)