"""Copy List With Random Pointer"""

class Node:
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class MyLinkedList:
    def __init__(self):
        self.nodes = 0
        self.head = Node()
    def get_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return -1
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current
    def add_at_index(self, index, val):
        if index < 0 or index > self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index):
            current = current.next
        new_node = Node(val, current.next)
        current.next = new_node
        self.nodes += 1
    def add_at_head(self, val):
        self.add_at_index(0, val)
    def add_at_tail(self, val):
        self.add_at_index(self.nodes, val)
    def delete_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.nodes -= 1
    def show_nodes(self):
        current = self.head
        for _ in range(self.nodes + 1 ):
            print(f"node: {current}, val: {current.val}, next: {current.next}, random: {current.random}")
            current = current.next
    def point_random(self, pointer_node_index, pointed_node_index):
        """random pointer points at some node or None"""
        if pointed_node_index is not None:
            self.get_at_index(pointer_node_index).random = self.get_at_index(pointed_node_index)
        else:
            self.get_at_index(pointer_node_index).random = None

# Testcases
l1 = MyLinkedList()
nodes1 = [7, 13, 11, 10, 1]
for node in nodes1:
    l1.add_at_tail(node)
l1.show_nodes()

# use pointer random to point some node
l1.point_random(0, None)
l1.point_random(1, 0)
l1.point_random(2, 4)
l1.point_random(3, 2)
l1.point_random(4, 0)
l1.show_nodes()
