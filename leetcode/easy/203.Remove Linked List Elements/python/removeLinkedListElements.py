"""Remove Linked List Elements"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.nodes = 0
        self.head = ListNode()
    def get_at_index(self, index):
        if index < 0 or index >= self.nodes:
            return -1
        current = self.head.next
        for _ in range(index):
            current = current.next
        return current.val
    def add_at_index(self, index, val):
        if index < 0:
            index = 0
        if index > self.nodes:
            return 
        current = self.head
        for _ in range(index):
            current = current.next
        node_added = ListNode(val)
        node_added.next = current.next
        current.next = node_added
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
    def remove_elements(self, head, val):
        '''Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)'''
        dummy = ListNode()
        dummy.next = head
        tortoise = dummy
        hare = dummy.next
        while hare is not None:
            if hare.val == val:
                while hare.val == val:
                    hare = hare.next
                    if hare is None:
                        break
                tortoise.next = hare
            if hare is not None:
                hare = hare.next
                if tortoise.next.val != val:
                    tortoise = tortoise.next
        return dummy.next


linked_list_a = LinkedList()
for i in range(1, 7):
    linked_list_a.add_at_tail(i)
linked_list_a.add_at_index(2, 6)
linked_list_a.show_nodes()
print(linked_list_a.remove_elements(linked_list_a.head.next, 6))

# Approach 2. Sentinel node and Two Pointer Technique
def remove_elements(head, val):
    sentinel = ListNode()
    sentinel.next = head
    prev, curr = sentinel, head
    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return sentinel.next

        