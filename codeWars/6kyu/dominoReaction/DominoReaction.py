def domino_reaction(dominos):
    bunchOfDominoes=""
    if dominos == "":
        return dominos
    for domino in dominos:
        if domino == "/" or domino == " ":
            return dominos
        else:
            numOfSuccess=0
            for secondDomino in dominos:
                if secondDomino == "|":
                    bunchOfDominoes+="/"
                    numOfSuccess+=1
                else:
                    bunchOfDominoes+=dominos[numOfSuccess:]
                    return bunchOfDominoes
            return bunchOfDominoes

print(domino_reaction("||| ||||//| |/"))


