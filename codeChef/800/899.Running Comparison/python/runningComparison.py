"""Running Comparison"""    
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    happy_days = 0
    for i in range(n):
        if a[i] <= 2 * b[i] and b[i] <= 2 * a[i]:
            happy_days += 1
    print(happy_days)
