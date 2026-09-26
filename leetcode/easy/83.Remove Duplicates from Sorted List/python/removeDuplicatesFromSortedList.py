"""Remove Duplicates From Sorted List"""

def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

def remove_duplicates(head):
    slow = fast = head
    while fast:
        start = fast
        while fast and slow.val == fast.val:
            fast = fast.next
        if start != fast:
            slow.next = fast
        else:
            slow = slow.next
    return head

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''