t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    amount = sum(b[i] for i in range(n) if a[i] >= x)
    print(amount)
    t -= 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''