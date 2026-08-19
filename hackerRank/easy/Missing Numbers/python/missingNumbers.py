# Missing Numbers

def missing_numbers(arr, brr):
    from collections import defaultdict
    count_arr = defaultdict(int)
    for num in arr:
        count_arr[num] += 1
    count_brr = defaultdict(int)
    for num in brr:
        count_brr[num] += 1
    ans = []
    for key in count_brr:
        if count_arr[key] < count_brr[key]:
            ans.append(key)
    return sorted(ans)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''