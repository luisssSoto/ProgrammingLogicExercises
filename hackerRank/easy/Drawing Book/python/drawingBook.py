"""Drawing Book"""

def pageCount(n, p):
    pages_from_beg = pages_from_end = 0
    first_page = 0
    last_page = n
    if n % 2 == 0:
        last_page += 1
    while True:
        if first_page == p or first_page + 1 == p:
            return pages_from_beg
        if last_page == p or last_page - 1 == p:
            return pages_from_end
        first_page += 2
        last_page -= 2
        pages_from_beg += 1
        pages_from_end += 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''