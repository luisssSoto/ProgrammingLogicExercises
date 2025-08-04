"""Remove Duplicates From Sorted List"""

def remove_duplicates(head):
    current = head
    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''