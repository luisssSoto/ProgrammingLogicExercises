"""+1 Array"""
def up_array(arr):
    length = len(arr)
    if length == 0:
        return None
    power = 10 ** (length - 1)
    result = 0
    for ele in arr:
        if power <= 1:
            result += 1
        if ele > 9 or ele < 0:
            return None
        ele *= power
        result += ele
        power //= 10
    new_arr = [int(letter) for letter in str(result)]
    if arr[0] == 0 and length > 1:
        zeroes = 0
        for ele in arr:
            if ele == 0:
                zeroes += 1
            else:
                break
        for _ in range(zeroes):
            new_arr.insert(0, 0)
    return (new_arr)

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(N)'''