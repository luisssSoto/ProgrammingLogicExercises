def strStr(haystack, needle):
    '''time complexity O(nm) Where n = lenght of haystack Where m = lenght of needle
       space complexity O(1)'''
    n = len(haystack)
    m = len(needle)
    for window_start in range(n - m + 1):
        for i in range(m):
            if needle[i] != haystack[window_start + i]:
                break
            if i == m - 1:
                return window_start
    return - 1

h = 'lietceet'
n = 'eet'
print(strStr(h, n))