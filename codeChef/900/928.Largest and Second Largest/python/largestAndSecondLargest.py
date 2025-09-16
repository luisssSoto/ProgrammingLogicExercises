"""Largest and Second Largest"""
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    greatest = max(a)
    greater = 0
    for val in a:
        if val > greater and val != greatest:
            greater = val
    print(greatest + greater)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''