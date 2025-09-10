"""Find Maximum in an Array"""
# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    mountains = list(map(int, input().split()))
    
    greater_height = mountains[0]
    for i in range(n):
        if mountains[i] > greater_height:
            greater_height = mountains[i]
    print(greater_height)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''