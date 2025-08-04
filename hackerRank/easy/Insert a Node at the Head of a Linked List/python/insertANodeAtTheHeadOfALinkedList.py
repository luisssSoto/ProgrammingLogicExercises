"""Insert a Node at the Head of a Linked List"""

class SinglyLinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def insertNodeAtHead(llist, data):
    head = SinglyLinkedListNode(data)
    head.next = llist
    return head

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''