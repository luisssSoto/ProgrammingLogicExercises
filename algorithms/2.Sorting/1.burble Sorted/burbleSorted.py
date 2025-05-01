"""Burble Sorted"""

def burble_sorted(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Testing
testData1 = [2,3,2,5,5,5,1,8,2,4,11]
print(burble_sorted(testData1))