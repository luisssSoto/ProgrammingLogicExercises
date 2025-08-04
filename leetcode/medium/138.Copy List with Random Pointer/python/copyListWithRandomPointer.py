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

def copy_random_list(head):
    if head is None:
        return head
    visited_nodes = {}
    def get_clone_node(node, created_nodes):
        if node is not None:
            if node in created_nodes:
                return created_nodes[node]
            else:
                created_nodes[node] = Node(node.val, None, None)
                return created_nodes[node]
        else:
            return None
    old_node = head
    new_node = Node(old_node.val, None, None)
    visited_nodes[old_node] = new_node
    while old_node is not None:
        new_node.random = get_clone_node(old_node.random, visited_nodes)
        new_node.next = get_clone_node(old_node.next, visited_nodes)
        new_node = new_node.next
        old_node = old_node.next
    return visited_nodes[head]

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''

print(copy_random_list(l1.head.next))