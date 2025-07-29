"Mini-Max Sum"

def mini_max_sum(arr):
    def burble_sort(arr):
        is_it_sorted = False
        while is_it_sorted == False:
            is_it_sorted = True
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    is_it_sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr
    arr = burble_sort(arr)
    min = sum(arr[0 : 4])
    max = sum(arr[1 : 5])
    print(min, max, sep=" ")

# Testing
arr1 = [2, 49, 32, 1, 8]
mini_max_sum(arr1)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

