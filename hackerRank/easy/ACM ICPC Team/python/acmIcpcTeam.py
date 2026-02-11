"""ACM ICPC Team"""

def acm_team(topic: list[str]) -> list[int]:
    max_ones = teams = 0
    topic = [int(x, 2) for x in topic]
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            combined_topics = topic[i] | topic[j]
            count_ones = combined_topics.bit_count()
            if count_ones > max_ones:
                max_ones = count_ones
                teams = 1
            elif count_ones == max_ones:
                teams += 1
    return [max_ones, teams]

# testcase
tc1 = ['10101', '11100', '11010', '00101']
print(acm_team(tc1))

'''Complexity Analysis:
Time Complexity: O(n^2 + nm)
Space Complexity: O(1)'''