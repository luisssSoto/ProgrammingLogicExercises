t = int(input())
for i in range(t):
    s = input()
    words = s.split()
    result = [word if word.isupper() else word.capitalize() for word in words]
    print(" ".join(result))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''