# 2260.Minimum Consecutive Cards to Pick Up

def minimum_card_pick_up(cards: list[int]) -> int:
    from collections import defaultdict
    val_idx = defaultdict(int)
    ans = float('inf')
    for i in range(len(cards)):
        if cards[i] in val_idx:
            ans = min(ans, i - val_idx[cards[i]] + 1)
        val_idx[cards[i]] = i
    return ans if ans < float('inf') else - 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''