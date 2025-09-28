"""Meeting Rooms"""

def canAttendMeetings(intervals: list[list[int]]) -> bool:
        meetings_hours = set()
        could_attend_all = True
        for interval in intervals:
            for i in range(interval[0], interval[1]):
                if i in meetings_hours:
                    could_attend_all = False
                    return could_attend_all
                else:
                    meetings_hours.add(i)
        print(meetings_hours)
        return could_attend_all
    

t1 = [[2, 4], [4, 6], [0, 3]]
print(canAttendMeetings(t1))

'''Complexity Analysis:
Time Complexity: O(N * M)
Space Complexity: O(N * M)
'''

def canAttendMeetings(intervals: list[list[int]]) -> bool:
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    print(intervals)
    return True

t1 = [[2, 4], [4, 6], [0, 3]]
print(canAttendMeetings(t1))

'''Complexity Analysis:
Time Complexity: O(N log N)
Space Complexity: O(N) because of sort() methon in Python'''