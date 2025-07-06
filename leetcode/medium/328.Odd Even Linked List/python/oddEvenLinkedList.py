"""Odd Even Linked List"""

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
    def add_ad_tail(self, val):
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
        for i in range(self.nodes):
            print(f"Node: {current}, val: {current.val}, next: {current.next}")
            current = current.next
    # Approach 1: One pass and Sentinel node
    def odd_even(self, head):
        '''Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)'''
        sentinel_node = ListNode(-1, head)
        current = head
        if head is None:
            return head
        even_head = head.next
        count = 1
        while current is not None:
            if current.next is None and count % 2 != 0:
                current.next = even_head
                break
            elif current.next.next is None and count % 2 != 0:
                tail_odd = current
                tail_odd.next = even_head
                break
            next_temp = current.next
            current.next = next_temp.next
            current = next_temp
            count += 1
        return sentinel_node.next

linked_list_a = MyLinkedList()
nodes_a = [2,1,3,5,6,4,7]
nodes_b = [x for x in range(1, 6)]
nodes_c = [x for x in range(1, 9)]
nodes_d = []
for node in nodes_d:
    linked_list_a.add_ad_tail(node)
linked_list_a.show_nodes()
print(linked_list_a.odd_even(linked_list_a.head.next))
linked_list_a.show_nodes()
