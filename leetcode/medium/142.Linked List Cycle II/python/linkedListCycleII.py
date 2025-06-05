"""Linked List Cycle II"""

# Approach 1. Hash Table
def detect_cycle(head):
    my_set = set()
    while head is not None:
        if head in my_set:
            return head
        my_set.add(head)
        head = head.next
    return None

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Approach 2: Floyd's Tortoise and Hare Algorithm
def detect_cycle(head):
    tortoise = head
    hare = head
    while hare and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        if hare == tortoise:
            hare = head
            while hare != tortoise:
                hare = hare.next
                tortoise = tortoise.next
            return tortoise
    return None
    

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''
