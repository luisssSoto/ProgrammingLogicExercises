# cook your dish here
n, x = map(int, input().split())
a = list(map(int, input().split()))

if x in a:
    print("YES")
else:
    print("NO")

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''