"""Design Doubly Linked List"""
class ListNode:
    def __init__(self, prev=None, val=0, next=None):
        self.prev = prev
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.nodes = 0
        self.head = ListNode()
    def get_at_index(self, index):
        '''int get(int index) Get the value of the indexth node 
        in the linked list. If the index is invalid, return -1.'''
        if index < 0 or index >= self.nodes:
            return -1
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.val
    def add_at_index(self, index, val):
        '''void add_at_index(int index, int val) Add a node of 
        value val before the indexth node in the linked list. 
        If index equals the length of the linked list, the node 
        will be appended to the end of the linked list. If index 
        is greater than the length, the node will not be inserted.'''
        if index < 0 or index > self.nodes:
            return 'Invalid Index'
        current = self.head
        for _ in range(index):
            current = current.next
        added_node = ListNode(current, val, current.next)
        if current.next is not None:
            current.next.prev = added_node
        current.next = added_node
        self.nodes += 1
    def add_at_head(self, val):
        '''void add_at_head(int val) Add a node of value val 
        before the first element of the linked list. After 
        the insertion, the new node will be the first node 
        of the linked list.'''
        self.add_at_index(0, val)
    def add_at_tail(self, val):
        '''void add_at_tail(int val) Append a node of value val 
        as the last element of the linked list.'''
        self.add_at_index(self.nodes, val)
    def delete_at_index(self, index):
        '''void delete_at_index(int index) Delete the indexth node 
        in the linked list, if the index is valid.'''
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
            print(f"node: {current}, prev: {current.prev}, val: {current.val}, next: {current.next}")
            current = current.next

# Testing 
nodes = [[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
linked_list_a = MyLinkedList()
for i in range(3):
    linked_list_a.add_at_head(nodes[i][0])
linked_list_a.add_at_index(nodes[3][0], nodes[3][1])
linked_list_a.show_nodes()
linked_list_a.delete_at_index(nodes[4][0])
linked_list_a.add_at_head(nodes[5][0])
linked_list_a.show_nodes()
linked_list_a.add_at_tail(nodes[6][0])
linked_list_a.show_nodes()
