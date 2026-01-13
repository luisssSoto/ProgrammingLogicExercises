"""Shortest Distance to a Character"""

def shortest_distance(s: str, c: str) -> list[int]:
    ans = []
    prev = float('-inf')
    for i in range(len(s)):
        if s[i] == c:
            prev = i
        ans.append(i - prev)
    print(ans)
    prev = float('inf')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev = i
        ans[i] = min(ans[i], prev - i)
    return ans

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# testcase
s1 = "loveleetcode"
c1 = "e"
print(shortest_distance(s1, c1))