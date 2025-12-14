"""Viral Advertising"""

def viral_advertising(n: int) -> int:
    shared = 5
    cum = liked = 0
    for _ in range(n):
        liked = shared // 2
        cum += liked
        shared = liked * 3
    return cum

'''Complexity Analysis: 
Time Complexity: O(1) Because constrainst max input is 50
Space Complexity: O(1)'''