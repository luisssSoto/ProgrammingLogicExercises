"""Shortest Word Distance"""

def shortest_distance(words_dict: list[str], word1: str, word2: str) -> int:
    freq = {word1: [], 
        word2: []}
    for i in range(len(words_dict)):
        if words_dict[i] == word1:
            freq[word1].append(i)
        elif words_dict[i] == word2:
            freq[word2].append(i)
    shortest_dis = float("inf")
    for ele in freq[word1]:
        for el in freq[word2]:
            if abs(ele - el) < shortest_dis:
                shortest_dis = abs(ele - el)
    return shortest_dis

'''Complexity Analysis:
Time Complexity: O(M * N)
Space Complexity: O(M + N)'''

def shortest_distance(words_dict: list[str], word1: str, word2: str) -> int:
    shortest_dis = float("inf")
    last_index_word1 = last_index_word2 = None
    for i in range(len(words_dict)):
        if words_dict[i] == word1:
            last_index_word1 = i
        elif words_dict[i] == word2:
            last_index_word2 = i
        if last_index_word1 is not None and last_index_word2 is not None:
            if abs(last_index_word1 - last_index_word2) < shortest_dis:
                shortest_dis = abs(last_index_word1 - last_index_word2)
    return shortest_dis

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''
