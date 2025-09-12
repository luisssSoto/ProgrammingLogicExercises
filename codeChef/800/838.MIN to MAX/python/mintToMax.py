"""MIN to MAX"""
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Your code goes here
    count = sum(1 for i in range(n) if a[i] != min(a))
    print(count)
    t -= 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''