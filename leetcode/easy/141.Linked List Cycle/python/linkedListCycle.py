"""Linked List Cycle"""

# Approach 1. Hash Table
def has_cycle(head):
    my_set = set()
    while head is not None:
        if head in my_set:
            return True
        my_set.add(head)
        head = head.next
    return False

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Approach 2: Floyd's Cycle Finding Algorithm

def has_cycle(head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''