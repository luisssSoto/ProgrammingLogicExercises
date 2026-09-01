# 2260.Minimum Consecutive Cards to Pick Up

def minimum_card_pick_up(cards: list[int]) -> int:
    val_idx = {}
    ans = len(cards)
    for i in range(len(cards)):
        if cards[i] not in val_idx:
            val_idx[cards[i]] = i
        else:
            diff = i - val_idx[cards[i]]
            if diff < ans:
                ans = diff
            val_idx[cards[i]] = i
    if ans == len(cards):
        return -1
    else:
        return ans + 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''