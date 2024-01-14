def solution(s):
    newString=""
    if len(s) == 0: return newString
    for element in s:
        if element == element.upper():newString+=" "+element
        else: newString+=element
    return newString

print(solution(''))