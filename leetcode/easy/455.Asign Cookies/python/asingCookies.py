"""Asing Cookies"""

def find_content_children(self, g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    content_children = 0
    children_index = 0
    cookie_index = 0
    while children_index < len(g) and cookie_index < len(s):
        if s[cookie_index] >= g[children_index]:
            content_children += 1
            children_index += 1
        cookie_index += 1
        
    return content_children

'''Complexity Analysis:
Time Complexity: O(N log N + M log M)
Space Complexity: O(N + M)'''