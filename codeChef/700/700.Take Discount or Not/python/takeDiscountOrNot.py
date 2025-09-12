"""Take Discount or Not"""
t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    without_coupon = sum(a)
    with_coupon = x + sum(max(0, val - y) for val in a)
    if with_coupon < without_coupon:
        print("COUPON")
    else:
        print("NO COUPON")

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''