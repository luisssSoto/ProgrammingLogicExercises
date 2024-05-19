" Find The Missing Element Between Two Arrays"
def find_missing(arr1, arr2):
    for element in arr1:
        if element not in arr2: return element
        else: arr2.remove(element)

a1 = [1, 2, 2, 3]
a2 = [1, 2, 3]
n1, n2 = [6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]
print(find_missing(a1, a2))
print(find_missing(n1, n2))
