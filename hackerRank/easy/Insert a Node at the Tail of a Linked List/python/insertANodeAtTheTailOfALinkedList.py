"""Insert a Node at the Tail of a Linked List"""

class SinglyLinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.nodes = 0
        self.head = SinglyLinkedListNode()
    def get(self, index):
        if index < 0 or index >= self.nodes:
            return -1
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.data
    def add_at_index(self, index, data):
        if index < 0 or index > self.nodes:
            return - 1
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = SinglyLinkedListNode(data, current.next)
        self.nodes += 1
    def add_at_head(self, data):
        self.add_at_index(0, data)
    def add_at_tail(self, data):
        self.add_at_index(self.nodes, data)
    def delete_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return - 1
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.nodes -= 1

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