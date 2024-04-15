#time started: 07:49
#time finished 08:06

def parse(data):
    array = []
    element = 0
    for letter in data:
        match letter:
            case 'i': element += 1
            case 'd': element -= 1
            case 's': element *= element
            case 'o': array.append(element)
    return array

value = 'iiisdoso'
print(parse(value))