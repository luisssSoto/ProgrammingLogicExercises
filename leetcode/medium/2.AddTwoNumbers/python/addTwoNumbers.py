"""Add Two Numbers"""

class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.nodes = 0
        self.head = ListNode()
    def get_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.val
    def add_at_index(self, index, val):
        if index < 0 or index > self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index):
            current = current.next
        new_node = ListNode(val, next=current.next)
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
        current = self.head.next
        for _ in range(self.nodes):
            print(f"Node: {current}, val: {current.val}, next: {current.next}")
            current = current.next
        print()

# Testing
nodes_a = [2,4,3]
linked_a = MyLinkedList()
for node in nodes_a:
    linked_a.add_at_tail(node)
linked_a.show_nodes()

nodes_b = [5,6,4]
linked_b = MyLinkedList()
for node in nodes_b:
    linked_b.add_at_tail(node)
linked_b.show_nodes()


def add_two_numbers(l1, l2):
    sentinel_node = ListNode()
    head = sentinel_node
    dec1 = 1
    result = 0
    while l1 is not None:
        result += l1.val * dec1
        dec1 *= 10
        l1 = l1.next
    dec2 = 1
    while l2 is not None:
        result += l2.val * dec2
        dec2 *= 10
        l2 = l2.next
    str_result = str(result)
    for i in range(len(str_result) - 1, -1, -1):
        head.next = ListNode(int(str_result[i]))
        head = head.next
    return sentinel_node.next

'''Complexity Analysis:
Time Complexity: O(Max(M,N))
Space Complexity: O(Max(M,N))'''

print(add_two_numbers(linked_a.head.next, linked_b.head.next))