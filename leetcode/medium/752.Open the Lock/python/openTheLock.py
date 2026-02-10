"""Open The Lock"""

def open_lock(deadends: list[str], target: str) -> int:
    next_slot = {str(x): str(x + 1) if x != 9 else '0' for x in range(10)}
    prev_slot = {str(x): str(x - 1) if x != 0 else '9' for x in range(10)}
    visited_combinations = set(deadends)
    pending_combinations = []
    turns = 0
    if "0000" in visited_combinations:
        return -1
    visited_combinations.add("0000")
    pending_combinations.append("0000")
    while pending_combinations:
        curr_level_len = len(pending_combinations)
        for _ in range(curr_level_len):
            curr_combination = pending_combinations.pop(0)
            if curr_combination == target:
                return turns
            for wheel in range(4):
                new_combination = list(curr_combination)
                new_combination[wheel] = next_slot[new_combination[wheel]]
                new_combination_str = "".join(new_combination)
                if new_combination_str not in visited_combinations:
                    pending_combinations.append(new_combination_str)
                    visited_combinations.add(new_combination_str)
                new_combination = list(curr_combination)
                new_combination[wheel] = prev_slot[new_combination[wheel]]
                new_combination_str = "".join(new_combination)
                if new_combination_str not in visited_combinations:
                    pending_combinations.append(new_combination_str)
                    visited_combinations.add(new_combination_str)
        turns += 1
    return -1


'''Complexity Analysis:
Here, n=10 is the number of slots on a wheel, w=4 is the number of wheels, and d is the 
number of elements in the deadends array.
Time complexity: O(4(d+10 4))
Space complexity: O(4(d+10 4))'''
