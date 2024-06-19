def solution(n):
    minutes = n % 60
    hours = n // 60
    if minutes == 0:
        return hours
    else:
        hours = str(hours)
        minutes = str(minutes)
        strValue = hours + minutes
        strValue = strValue.replace('', '-')
        newValue = 0
        for element in strValue:
            if element.isnumeric():
                newValue += int(element)
        return newValue

test = 808

print(solution(test))