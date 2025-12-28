"""Circular Array Rotation"""

def circularArrayRotation(a: int, k: int, queries: list) -> list:
    '''Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(1)'''
    ans = []
    for query in queries:
        print((query - k) % len(a))
        ans.append(a[(query - k) % len(a)])
    return ans

a = [x for x in range(1, 6)]
print(a)
print(circularArrayRotation(a, 4, [x for x in range(5)]))

def circularArrayRotation(a: int, k: int, queries: list) -> list:
    '''Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(N)'''    
    right_places = len(a) - (k % len(a))
    a += a[:right_places]
    a = a[right_places:]
    ans = []
    for query in queries:
        ans.append(a[query])
    return ans
    
def circularArrayRotation(a: int, k: int, queries: list) -> list:
    '''Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(N)'''
    right_places = len(a) - (k % len(a))
    modified_a = a[right_places:]
    modified_a += a[:right_places]
    ans = []
    for query in queries:
        ans.append(modified_a[query])
    return ans

def circularArrayRotation(a: int, k: int, queries: list) -> list:
    '''Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(N)'''
    right_places = len(a) - (k % len(a))
    modified_a = []
    ans = []
    print(right_places)
    for i in range(right_places, len(a), 1):
        modified_a.append(a[i])
    print(modified_a)
    for i in range(right_places):
        modified_a.append(a[i])
    print(modified_a)
    for query in queries:
        ans.append(modified_a[query])
    return ans
    
def circularArrayRotation(a: int, k: int, queries: list) -> list:
    '''Complexity Analysis:
    Time Complexity: O(N2)
    Space Complexity: O(1)'''
    right_places = k % len(a)
    ans = []
    print(right_places)
    for i in range(right_places):
        last_element = a[-1]
        for j in range(len(a) - 1, 0, -1):
            a[j] = a[j - 1]
        a[0] = last_element
    print(f"modified array: {a}")
    for query in queries:
        ans.append(a[query])
    return ans