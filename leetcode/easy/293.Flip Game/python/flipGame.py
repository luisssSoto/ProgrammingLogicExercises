"""Flip Game"""

def generate_possible_new_moves(currentState: str) -> list[str]:
    ans = []
    current_st_list = [ch for ch in currentState]
    print(current_st_list)
    for i in range(len(currentState) - 1):
        if current_st_list[i] == '+' and current_st_list[i + 1] == '+':
            current_st_list[i] = '-'
            current_st_list[i + 1] = '-'
            state = "".join(current_st_list)
            ans.append(state)
            current_st_list[i] = '+'
            current_st_list[i + 1] = '+'
    return ans

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(N)'''

def generate_possible_new_moves(currentState: str) -> list[str]:
    ans = []
    for i in range((len(currentState) - 1)):
        if currentState[i] == '+' and currentState[i + 1] == '+':
            state = currentState[:i] + '--' + currentState[i + 2:]
            ans.append(state)
    return ans

'''Complexity Analysis: 
Time Complexity: O(N2)
Space Complexity: O(1)'''