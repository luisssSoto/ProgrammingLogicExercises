"""Daily Temperatures"""

def daily_temp(temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)
    stack = []
    for current_day, current_temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < current_temp:
            previous_day = stack.pop()
            ans[previous_day] = current_day - previous_day
        stack.append(current_day)
    return ans

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''