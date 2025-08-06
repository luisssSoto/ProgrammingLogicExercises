"""Between Two Sets"""

def get_total_x(a, b):
    max_a = max(a)
    min_b = min(b)
    possible_values = [x for x in range(max_a, min_b + 1)]
    matches = 0
    for i in range(len(possible_values)):
        fail = False
        for j in range(len(a)):
            if possible_values[i] % a[j] != 0:
                fail = True
                break
        if fail is True:
            continue
        for j in range(len(b)):
            if b[j] % possible_values[i] != 0:
                fail = True
                break
        if fail is True:
            continue
        matches += 1
    return matches

'''Complexity Analysis:
Time Complexity: O(N * M + N * L)
Space Complexity O(1)'''