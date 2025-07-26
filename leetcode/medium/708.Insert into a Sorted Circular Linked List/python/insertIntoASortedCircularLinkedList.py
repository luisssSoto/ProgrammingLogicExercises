"""Insert into a Sorted Circular Linked List"""
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
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
        new_node = Node(val, current.next)
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
        for _ in range(self.nodes + 1):
            print(f"Node: {current}, val: {current.val}, next: {current.next}")
            current = current.next
    def make_it_circular(self):
        first_node = self.head.next
        current = self.head.next
        for _ in range(self.nodes - 1):
            current = current.next
        current.next = first_node

# Testcase
nodes1 = [1,3,5]
l1 = MyLinkedList()
for node in nodes1:
    l1.add_at_tail(node)
l1.show_nodes()
l1.make_it_circular()
l1.show_nodes()
insert_val = 2

l3 = MyLinkedList()
l3.add_at_tail(1)
l3.show_nodes()
l3.make_it_circular()



def insert_into_circular(head, insertVal):  
    if head == None:
        newNode = Node(insertVal, None)
        newNode.next = newNode
        return newNode
    
    prev, curr = head, head.next
    toInsert = False

    while True:
            
        if prev.val <= insertVal <= curr.val:
            # Case #1.
            toInsert = True
        elif prev.val > curr.val:
            # Case #2. where we locate the tail element
            # 'prev' points to the tail, i.e. the largest element!
            if insertVal >= prev.val or insertVal <= curr.val:
                toInsert = True

        if toInsert:
            prev.next = Node(insertVal, curr)
            # mission accomplished
            return head

        prev, curr = curr, curr.next
        # loop condition
        if prev == head:
            break
    # Case #3.
    # did not insert the node in the loop
    prev.next = Node(insertVal, curr)
    return head

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity O(1)'''

print(insert_into_circular(l1.head.next, insert_val))
