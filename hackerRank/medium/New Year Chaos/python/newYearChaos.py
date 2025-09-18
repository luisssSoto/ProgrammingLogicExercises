"""New Year Chaos"""

def minimum_bribes(q):
    # Write your code here
    sorted_q = sorted(q)
    total_bribes = 0
    for i in range(len(q)):
        if q[i] != sorted_q[i]:
            indv_bribes = 0 
        for j in range(i, len(sorted_q)):
            if q[i] != sorted_q[j]:
                indv_bribes += 1
                total_bribes += 1
            else:
                temp = sorted_q[j]
                del sorted_q[j]
                sorted_q.insert(i, temp)
                break
            if indv_bribes > 2:
                print('Too chaotic')
                return
    print(total_bribes)
    return

'''Complexity Analysis:
Time Complexity O(N * N)
Space Complexity: O(N)'''