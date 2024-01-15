def possibly_perfect(key, answers):
    countBest, countWorst = 0, 0
    numberOfMatches=len(answers)
    for number in range(numberOfMatches):
        if key[number] == "_":
            countBest+=1
            countWorst+=1
            continue
        if answers[number] == key[number]: countBest+=1
        elif answers[number] != key[number]: countWorst+=1
    if countBest == len(key) or countWorst == len(key): return True
    else: return False

k='_'
k=k.split()
print(k)
a='a'
a=a.split()
print(a)
print(possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B']))
