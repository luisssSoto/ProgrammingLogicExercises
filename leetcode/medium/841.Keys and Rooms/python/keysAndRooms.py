"""Keys and Rooms"""

def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    from collections import deque
    
    queue = deque()
    seen = set()
    seen.add(0)
    for room in rooms[0]:
        if room not in seen:
            queue.append(room)
            seen.add(room)
    num_rooms = len(rooms)
    count = len(queue) + 1
    if count == num_rooms:
        return True
    while queue:
        room = queue.popleft()
        for k in rooms[room]:
            if k not in seen:
                seen.add(k)
                queue.append(k)
                count += 1
            if count == num_rooms:
                return True
    return False

'''Complexity Analysis:
Time Complexity: O(N + E) where N is the number of rooms, and E is the total number of keys.
Space Complexity: O(N) in additional space complexity, to store queue and seen.'''
    