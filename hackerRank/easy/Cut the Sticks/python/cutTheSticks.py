"""Cut the Sticks"""

def cut_sticks(arr: list[int]) -> list[int]:
    ans = []
    arr.sort()
    while len(arr) >= 1:
        start_point = 0
        min_val = arr[0]
        for i in range(len(arr)):
            res = arr[i] - min_val
            arr[i] = res
            if res <= 0:
                start_point = i + 1
        ans.append(len(arr))
        arr = arr[start_point: ]
    return ans

'''Complexity Analysis:
Time Complexity: O(log N)
Space Complexity: O(N)'''