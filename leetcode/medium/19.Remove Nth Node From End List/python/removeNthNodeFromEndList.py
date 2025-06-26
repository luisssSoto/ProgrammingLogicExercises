"""Remove Nth Node From End List"""

class Node():
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.nodes = 0
        self.head = Node()
    def get_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return 'Invalid Index'
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
        new_node = Node(val)
        new_node.next = current.next
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
        for i in range(self.nodes + 1):
            print(f'current node: {current}, val: {current.val}, next: {current.next}')
            current = current.next
        print()
    # Approach 1: List
    def remove_nth_from_end_1(self, head, n):
        """Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(N)"""
        nodes_list = []
        dummy = Node(0, None)
        dummy.next = head
        while head is not None:
            nodes_list.append(head)
            head = head.next
        pointer_to_delete = len(nodes_list) - n
        predecessor_pointer = pointer_to_delete - 1
        if predecessor_pointer < 0:
            return dummy.next.next
        predecessor = nodes_list[predecessor_pointer]
        successor = nodes_list[pointer_to_delete].next
        predecessor.next = successor
        self.nodes -= 1
        return dummy.next
    # Approach 2: Two Pass Algorithm
    def remove_nth_from_end_2(self, head, n):
        """Complexity Analysis:
        Time Complexity: O(L)
        Space Complexity: O(1)"""
        dummy = Node(0, None)
        dummy.next = head
        first = head
        length = 0
        while first is not None:
            first = first.next
            length += 1
        length -= n
        first = dummy
        while length > 0:
            first = first.next
            length -= 1
        first.next = first.next.next
        self.nodes -= 1
        return dummy.next
    # Approach 3: Two Pointers Technique
    def remove_nth_from_end_3(self, head, n):
        """Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)"""
        dummy = Node()
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n + 1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        self.nodes -= 1
        return dummy.next

# Testing 1
linked_list_a = LinkedList()
data_a = [x + 1 for x in range(5)]
for val in data_a:
    linked_list_a.add_at_tail(val)
linked_list_a.show_nodes()
linked_list_a.remove_nth_from_end_1(linked_list_a.head.next, 2)
linked_list_a.show_nodes()

# Testing 2
linked_list_b = LinkedList()
linked_list_b.add_at_tail(1)
linked_list_b.show_nodes()
linked_list_b.remove_nth_from_end_2(linked_list_b.head.next, 1)
linked_list_b.show_nodes()

# Testing 3
linked_list_c = LinkedList()
for i in range(1, 3):
    linked_list_c.add_at_tail(i)
linked_list_c.show_nodes()
linked_list_c.remove_nth_from_end_3(linked_list_c.head.next, 1)
linked_list_c.show_nodes()
