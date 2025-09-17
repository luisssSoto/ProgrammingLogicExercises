"""Difficulty Rating Order"""
t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    result = "Yes"
    for i in range(n - 1):
        if d[i] > d[i + 1]:
            result = "No"
            break
    print(result)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''