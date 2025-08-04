"""Apple and Orange"""

def apple_and_orange(s, t, a, b, apples, oranges):
    countApples = countOranges = 0
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            countApples += 1
    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            countOranges += 1
    print(countApples)
    print(countOranges)

'''Complexity Analysis:
Time Complexity: O(N + M)
Space Complexity: O(1)'''
