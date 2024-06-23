"""Finding Length Of The Sequence"""
def length_of_sequence(arr,n):
    if n in arr and arr.count(n) == 2: return len(arr[arr.index(n) : arr.index(n, arr.index(n)+1)+1])
    else: return 0
    
test = [0, -3, 7, 4, 0, 3, 7, 9]
print(length_of_sequence(test, 7)) 


