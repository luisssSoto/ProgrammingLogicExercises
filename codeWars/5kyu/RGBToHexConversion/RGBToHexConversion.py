"""RGB To Hex Conversion"""

def rgb(r, g, b):
    # create a variable string to keeps the final result
    decIntoHex = ''
    
    # create a variable which will be a list to keep each value like decimalThe rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
    decList = []
    decList = [r, g, b]

    #create a variable which will be a list to keep each value into hex
    hexList = []

    # iterate the decList
    for decimal in decList:
        # create a variable which save the each element of the decList
        hexNum = ''
        #conditional to validate if the decimal is an allow value
        if decimal > 0 and decimal <= 255:
            # add decimal value to hexNum and cast to hexadecimal
            hexNum = hex(decimal)
            if len(hexNum) < 4:
                hexNum = hexNum[0] + hexNum[-1].upper()
            else:
                hexNum = hexNum[-2].upper() + hexNum[-1].upper()
        else:
            #conditional if decimal < 0 so...
            if decimal <= 0 :
                hexNum = hex(0)
                hexNum = hexNum[0] + hexNum[-1].upper()
            #conditional if decimal > 255 so...
            else:
                hexNum = hex(255)
                hexNum = hexNum[-2].upper() + hexNum[-1].upper()
        # then, append it to the hexList
        hexList.append(hexNum)
    
    # unpacking the elements of hexList
    strR, strG, strB = hexList

    #concatenate them in decIntoHex
    decIntoHex += strR + strG + strB

    #return the final variable
    return decIntoHex

print(rgb(255, 0, 148))