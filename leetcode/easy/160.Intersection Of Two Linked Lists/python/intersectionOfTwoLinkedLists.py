"""Intersection of Two Linked Lists"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import copy
class LinkedList:
    def __init__(self):
        self.nodes = 0
        self.head = ListNode()
    def get_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return -1 
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.val
    def add_at_index(self, index, val):
        if index < 0:
            index = 0
        elif index > self.nodes:
            return
        next_node = ListNode(val)
        current = self.head
        for _ in range(index):
            current = current.next
        next_node.next = current.next
        current.next = next_node
        self.nodes += 1
    def add_at_head(self, val):
        self.add_at_index(0, val)
    def add_at_tail(self, val):
        self.add_at_index(self.nodes, val)
    def delete_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.nodes -= 1
    def show_nodes(self):
        current = self.head
        for i in range(self.nodes + 1):
            print(f'current node: {current}, val: {current.val}, next: {current.next}')
            current = current.next
        print()
    def add_linked_list(self, linked_list):
        last_node = self.head
        for _ in range(self.nodes):
            last_node = last_node.next
        last_node.next = linked_list.head.next
        copy_linked_list = copy.deepcopy(linked_list)
        while copy_linked_list.head.next is not None:
            self.nodes += 1
            copy_linked_list.head.next = copy_linked_list.head.next.next

# Testing
linked_list_a = LinkedList()
nodes_a = [4, 1]
for i in range(len(nodes_a)):
    linked_list_a.add_at_tail(nodes_a[i])
linked_list_a.show_nodes()
print()

linked_list_b = LinkedList()
nodes_b = [5, 6, 1]
for i in range(len(nodes_b)):
    linked_list_b.add_at_tail(nodes_b[i])
linked_list_b.show_nodes()
print()

linked_list_c = LinkedList()
nodes_c = [8, 4, 5]
for i in range(len(nodes_c)):
    linked_list_c.add_at_tail(nodes_c[i])
linked_list_c.show_nodes()

print(f'add linked list')
linked_list_a.add_linked_list(linked_list_c)
linked_list_a.show_nodes()
print()
linked_list_b.add_linked_list(linked_list_c)
linked_list_b.show_nodes()
print()
linked_list_c.show_nodes()

# Approach 1: Two Pointers
def get_intersection_node(headA, headB):
    h_a = headA
    h_b = headB
    nodes_a = 0
    while headA is not None:
        headA = headA.next
        nodes_a += 1
    nodes_b = 0
    while headB is not None:
        headB = headB.next
        nodes_b += 1
    greater_linked_list_head = ListNode()
    lesser_linked_list_head = ListNode()
    if nodes_a > nodes_b: 
        greater_linked_list_head = h_a
        lesser_linked_list_head = h_b
    elif nodes_a < nodes_b:
        greater_linked_list_head = h_b
        lesser_linked_list_head = h_a
    else:
            greater_linked_list_head = h_a
            lesser_linked_list_head = h_b
    start_pointer = abs(nodes_a - nodes_b)
    for _ in range(start_pointer):
        greater_linked_list_head = greater_linked_list_head.next
    while greater_linked_list_head is not None:
        if greater_linked_list_head == lesser_linked_list_head:
            return greater_linked_list_head
        greater_linked_list_head = greater_linked_list_head.next
        lesser_linked_list_head = lesser_linked_list_head.next

print(get_intersection_node(linked_list_a.head.next, linked_list_b.head.next))

'''Complexity Analysis
Let N be the length of list A and M be the length of list B.
Time complexity : O(N+M).
Space complexity : O(1).'''

# Approach 2. Hash Table

def get_intersection_node(headA, headB):
    unique_nodes = set()
    while headA is not None:
        if headA not in unique_nodes:
            unique_nodes.add(headA)
        headA = headA.next
    while headB is not None:
        if headB in unique_nodes:
            return headB
        headB = headB.next
    return None

# Prepare the input data
linked_list_a = LinkedList()
nodes_a = [1,9,1]
for node in nodes_a:
    linked_list_a.add_at_tail(node)
linked_list_a.show_nodes()

linked_list_b = LinkedList()
nodes_b = [3]
for node in nodes_b:
    linked_list_b.add_at_tail(node)
linked_list_b.show_nodes()

linked_list_c = LinkedList()
nodes_c = [2, 4]
for node in nodes_c:
    linked_list_c.add_at_tail(node)
linked_list_c.show_nodes()

# Intersection of the two linked lists
linked_list_a.add_linked_list(linked_list_c)
linked_list_b.add_linked_list(linked_list_c)

# Show the new two linked lists
linked_list_a.show_nodes()
linked_list_b.show_nodes()

# Testing
print(get_intersection_node(linked_list_a.head.next, linked_list_b.head.next))

'''Complexity Analysis:
Time Complexity: O(N + M)
Space Complexity: O(N)'''