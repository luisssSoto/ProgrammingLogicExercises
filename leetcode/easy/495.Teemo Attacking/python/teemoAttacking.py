"""Teemo Attacking"""

def teemo_attacking(time_series: list[int], duration: int)-> int:
    seconds = 0
    for i in range(len(time_series) - 1):
        if time_series[i] + duration > time_series[i + 1]:
            seconds += time_series[i + 1] - time_series[i]
        else:
            seconds += duration
    seconds += duration
    return seconds

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

# Same approach: but writting different
def teemo_attacking(time_series: list[int], duration: int)-> int:
    seconds = 0
    for i in range(len(time_series) - 1):
        seconds = min(time_series[i + 1] - time_series[i], duration)
    seconds += duration
    return seconds

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''