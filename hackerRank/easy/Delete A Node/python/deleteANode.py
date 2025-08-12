"""Delete A Node"""
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


def delete_node(llist, position):
    prev = llist
    if position == 0:
        llist = llist.next
        return llist       
    for _ in range(position - 1):
        prev = prev.next
    prev.next = prev.next.next
    return llist
