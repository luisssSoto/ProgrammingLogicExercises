"""Insert A Node At Specific Position In A Linked List"""

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
    def addAtIndex(self, index, data):
        if index < 0 or index > self.nodes:
            return - 1
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = SinglyLinkedListNode(data, current.next)
        self.nodes += 1
    def addAtHead(self, data):
        self.addAtIndex(0, data)
    def addAtTail(self, data):
        self.addAtIndex(self.nodes, data)
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.nodes:
            return - 1
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.nodes -= 1
        
    
    
def insert_node_at_position(llist, data, position):
    sentinel_node = llist
    for i in range(position - 1):
        sentinel_node = sentinel_node.next
    temp_node = sentinel_node.next
    new_node = SinglyLinkedListNode(data)
    sentinel_node.next = new_node
    new_node.next = temp_node
    return llist
