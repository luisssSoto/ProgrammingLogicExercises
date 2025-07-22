"""Flatten a Multilevel Doubly Linked List"""

class Node:
    def __init__(self, val=-1, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class MyDoublyLinkedList:
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
        new_node = Node(val, current, current.next, None)
        if current.next is not None:
            current.next.prev = new_node
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
        for _ in range(index + 1):
            current = current.next
        if current.next is not None:
            current.next.prev = current.prev
        current.prev.next = current.next
        self.nodes -= 1
    def show_nodes(self):
        current = self.head
        for _ in range(self.nodes + 1):
            print(f"Node: {current}, prev: {current.prev}, val: {current.val}, next: {current.next}, child: {current.child}")
            if current.child is not None:
                current_child = current.child
                while current_child is not None:
                    print(f"Node: {current_child}, prev: {current_child.prev}, val: {current_child.val}, next: {current_child.next}, child: {current_child.child}")
                    if current_child.child is not None:
                        current_grand_child = current_child.child
                        while current_grand_child is not None:
                            print(f"Node: {current_grand_child}, prev: {current_grand_child.prev}, val: {current_grand_child.val}, next: {current_grand_child.next}, child: {current_grand_child.child}")
                            current_grand_child = current_grand_child.next
                    current_child = current_child.next
            current = current.next
        print()
    def add_child(self, index, linked_list):
        current = self.get_at_index(index)
        current.child = linked_list

# Prepare the data
first_level_nodes = [x for x in range(1,7)]
first_linked = MyDoublyLinkedList()
for node in first_level_nodes:
    first_linked.add_at_tail(node)
first_linked.show_nodes()

second_level_nodes = [x for x in range(7, 11)]
second_linked = MyDoublyLinkedList()
for node in second_level_nodes:
    second_linked.add_at_tail(node)
second_linked.show_nodes()

third_level_nodes = [11, 12]
third_linked = MyDoublyLinkedList()
for node in third_level_nodes:
    third_linked.add_at_tail(node)
third_linked.show_nodes()

# Adding a child at the first linked list
first_linked.add_child(2, second_linked.head.next)
second_linked.add_child(1, third_linked.head.next)
first_linked.show_nodes()
# second_linked.show_nodes()

def flatten(head):
    sentinel_node = head
    current = head
    parent_nodes = []
    first_nodes = []
    while current is not None:
        if current.child is not None:
            parent_nodes.append(current)
            first_nodes.append(current.child)
            current = current.child
        else:
            if current.next is None:
                last_node = current
            current = current.next
        if current is None and len(parent_nodes) > 0:
            current = parent_nodes.pop()
            current.child = None
            last_node.next = current.next
            if current.next is not None:
                current.next.prev = last_node
            first_node = first_nodes.pop()
            current.next = first_node
            first_node.prev = current
            current = last_node
    return sentinel_node

print(flatten(first_linked.head.next))

l1 = MyDoublyLinkedList()
l1.add_at_tail(1)
l2 = MyDoublyLinkedList()
l2.add_at_tail(2)
l3 = MyDoublyLinkedList()
l3.add_at_tail(3)
l1.add_child(0, l2.head.next)
l2.add_child(0, l3.head.next)
l1.show_nodes()

print(flatten(l1.head.next))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''