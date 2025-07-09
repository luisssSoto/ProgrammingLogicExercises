"""Palindrome Linked List"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:
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
        if index < 0 or index > self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index):
            current = current.next
        added_node = ListNode(val, next=current.next)
        current.next = added_node
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

# Approach 1: 
def is_palindrome(head):
    if head.next is None:
        return True
    nodes_list = []
    while head is not None:
        nodes_list.append(head.val)
        head = head.next
    left_pointer = 0
    right_pointer = len(nodes_list) - 1
    while left_pointer < right_pointer:
        if nodes_list[left_pointer] != nodes_list[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''


# Testing
data_a = [1,2,2,1]
linked_list_a = MyLinkedList()
for node in data_a:
    linked_list_a.add_at_tail(node)
print(is_palindrome(linked_list_a.head.next))