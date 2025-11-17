"""Shortest Completing Word"""

def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    from collections import Counter
    licensePlate = "".join(list(filter(lambda ch: ch.isalpha(), licensePlate))).lower()
    license_plate_dict = Counter(licensePlate)
    winners = {}
    min_length = 15
    for word in words:
        flag = True
        word_dict = Counter(word)
        for key, val in license_plate_dict.items():
            if key in word_dict:
                if val > word_dict[key]:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            if len(word) not in winners:
                winners[len(word)] = [word]
            if len(word) < min_length:
                min_length = len(word)
            else:
                winners[len(word)].append(word)
    return winners[min_length][0]

'''Complexity Analysis:
Time Complexity: O(N * M)
Space Complexity: O(1)'''