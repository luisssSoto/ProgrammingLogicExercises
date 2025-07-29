"""Insert a Node at the Tail of a Linked List"""

class SinglyLinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    pnt = head
    while pnt.next is not None:
        pnt = pnt.next
    pnt.next = SinglyLinkedListNode(data)
    return head

'''Complexity Analysis: 
Time Complexity: O(N)
Space Complexity: O(1)'''