"""Breaking the Records"""

def breaking_records(scores):
    # Write your code here
    best_score = worst_score = scores[0]
    record = [0, 0]
    for score in scores:
        if score > best_score:
            best_score = score
            record[0] += 1
        if score < worst_score:
            worst_score = score
            record[1] += 1
    return record

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''