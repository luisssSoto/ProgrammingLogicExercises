"""Wordle"""
# cook your dish here
tc = int(input())
while tc > 0:
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] == t[i]:
            print("G", end="")
        else:
            print("B", end="")
    print()
    tc -= 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''