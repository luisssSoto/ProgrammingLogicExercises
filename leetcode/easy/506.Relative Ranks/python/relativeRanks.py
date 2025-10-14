"""Relative Ranks"""

def relative_ranks(score: list[int])-> list[str]:
    sorted_score = sorted(score, reverse=True)
    medal_score = {}
    for i in range(len(sorted_score)):
        if i == 0:
            medal_score[sorted_score[i]] = "Gold Medal"
        elif i == 1:
            medal_score[sorted_score[i]] = "Silver Medal"
        elif i == 2:
            medal_score[sorted_score[i]] = "Bronze Medal"
        else:
            medal_score[sorted_score[i]] = str(i + 1)
    answer = []
    for s in score:
        answer.append(medal_score[s])
    return answer

'''Complexity Analysis:
Time Complexity: O(N log N)
Space Complexity: O(N)'''