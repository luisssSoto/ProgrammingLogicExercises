"""Swap Nodes in Pairs"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class LinkedList:
# MyLinkedList() Initializes the MyLinkedList object.
    def __init__(self):
        self.head = ListNode()
        self.nodes = 0
# int get(int index) Get the value of the indexth node in the 
# linked list. If the index is invalid, return -1.
    def get(self, index):
        if index < 0 or index >= self.nodes:
            return - 1
        else: 
            predecessor = self.head
            for i in range(index + 1):
                predecessor = predecessor.next
            return predecessor.val
# void addAtIndex(int index, int val) Add a node of value val 
# before the indexth node in the linked list. If index equals 
# the length of the linked list, the node will be appended to 
# the end of the linked list. If index is greater than the length, 
# the node will not be inserted.
    def add_at_index(self, index, val):
        if index < 0:
            index = 0
        if index > self.nodes:
            return
        next_node = ListNode(val)
        self.nodes += 1
        predecessor = self.head
        for i in range(index):
            predecessor = predecessor.next
        next_node.next = predecessor.next
        predecessor.next = next_node
# void addAtHead(int val) Add a node of value val before the first 
# element of the linked list. After the insertion, the new node 
# will be the first node of the linked list.
    def add_at_head(self, val):
        self.add_at_index(0, val)
# void addAtTail(int val) Append a node of value val as the last 
# element of the linked list.
    def add_at_tail(self, val):
        self.add_at_index(self.nodes, val)
# void deleteAtIndex(int index) Delete the indexth node in the 
# linked list, if the index is valid.
    def delete_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return
        else:
            self.nodes -= 1
            predecessor = self.head
            for _ in range(index):
                predecessor = predecessor.next
            predecessor.next = predecessor.next.next
    def show_values(self):
        current = self.head
        for _ in range(self.nodes + 1):
            print(current.val, end=' | ')
            current = current.next
        print()

myLinkedList = LinkedList()
print(myLinkedList)
print(myLinkedList.head)
print(myLinkedList.add_at_head(1))
print(myLinkedList.get(0))
myLinkedList.add_at_tail(2)
print(myLinkedList)
print(myLinkedList.get(1))
myLinkedList.add_at_tail(3)
myLinkedList.add_at_tail(4)
myLinkedList.add_at_tail(5)
print(myLinkedList)
myLinkedList.show_values()
print()

def swap_nodes_in_pairs(head):
    dummy = ListNode(-1, None)
    dummy.next = head

    prev_node = dummy
    
    while head is not None and head.next is not None:
        first_node = head
        second_node = head.next

        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev_node = first_node
        head = first_node.next
    return dummy.next

myLinkedList.show_values()
swap_nodes_in_pairs(myLinkedList.head)

# Complexity Analysis:
# Time Complexity : O(N) where N is the size of the linked list.
# Space Complexity : O(1).