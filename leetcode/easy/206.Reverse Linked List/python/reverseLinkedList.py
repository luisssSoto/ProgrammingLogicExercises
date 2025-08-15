"""Reverse Linked List"""

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.nodes = 0
        self.head = ListNode()
    def get_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current
    def add_at_index(self, val, index):
        if index < 0 or index > self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index):
            current = current.next
        next_node = ListNode(val)
        next_node.next = current.next
        current.next = next_node
        self.nodes += 1
    def add_at_head(self, val):
        self.add_at_index(val, 0)
    def add_at_tail(self, val):
        self.add_at_index(val, self.nodes)
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
        while current is not None:
            print(f"Node: {current}, value: {current.val}, next: {current.next}")
            current = current.next
    def reverse_list(self, head):
        '''Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)'''
        first = head
        while first is not None and first.next is not None:
            temp = first.next
            first.next = temp.next
            temp.next = head
            head = temp
        # Testing
        while head is not None:
            print(f"Node: {head}, value: {head.val}, next: {head.next}")
            head = head.next


linked_list_a = LinkedList()
for i in range(1, 6):
    linked_list_a.add_at_tail(i)
linked_list_a.show_nodes()
linked_list_a.reverse_list(linked_list_a.head.next)

# Approach 1: One pass
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# Approach 2: Recursion
def reverse_linked_list(head):
    if (not head) or (not head.next):
            return head
    p = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return p

'''Complexity Analysis
Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).
Space complexity : O(n).
The extra space comes from implicit stack space due to recursion. 
The recursion could go up to n levels deep.'''

def r(head):
    curr = head
    prev = None
    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

linked_list_b = LinkedList()
for i in range(1, 6):
    linked_list_b.add_at_tail(i)
linked_list_b.show_nodes()
# print(r(linked_list_b.head.next))

def reverse_recursive(head):
    if (not head) or (not head.next):
        return head
    p = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return p

print(reverse_recursive(linked_list_b.head.next))