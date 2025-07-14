"""Merge Two Sorted Lists"""
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
        added_node = ListNode(val, current.next)
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
    def show_nodes(self):
        current = self.head
        for _ in range(self.nodes + 1):
            print(f"Node: {current}, val: {current.val}, next: {current.next}")
            current = current.next
        print()

# Testing
first_list = MyLinkedList()
first_nodes = [1,2,4]
for node in first_nodes:
    first_list.add_at_tail(node)
first_list.show_nodes()

second_list = MyLinkedList()
second_nodes = [1,3,4]
for node in second_nodes:
    second_list.add_at_tail(node)
second_list.show_nodes()

def merge_two_sorted_lists(list1, list2):
    sentinel_node = ListNode(-1)
    prev = sentinel_node
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next
    prev.next = list1 if list1 is not None else list2
    return sentinel_node.next

'''Complexity Analysis:
Time Complexity: O(n + m)
Space Complexity: O(1)'''
            

print(merge_two_sorted_lists(first_list.head.next, second_list.head.next))