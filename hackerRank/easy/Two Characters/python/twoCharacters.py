# Two Characters

def alternate(s: str) -> int:
    unique = list(set(s))
    max_len = 0
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            first = unique[i]
            second = unique[j]
            filtered = []
            for ch in s:
                if ch == first or ch == second:
                    filtered.append(ch)
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    valid = False
                    break
            if valid:
                max_len = max(max_len, len(filtered))
    return max_len


# Testcase
s1 = 'beabeefeab'
s2 = 'bbba'
print(alternate(s2))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''
            
