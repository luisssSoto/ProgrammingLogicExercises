"""Rotate List"""

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
        current = self.head
        for i in range(self.nodes + 1):
            print(f"Node: {current}, val: {current.val}, next: {current.next}")
            current = current.next

# Prepare data
ll_a = MyLinkedList()
nodes_a = [x for x in range(1, 6)]
for node in nodes_a:
    ll_a.add_ad_tail(node)
ll_a.show_nodes()
places = 2

def rotate_right(head, k):
    if head is None:
        return head
    sentinel_node = head
    copy_ll = []
    while sentinel_node is not None:
        copy_ll.append(sentinel_node)
        sentinel_node = sentinel_node.next
    real_places = k % len(copy_ll)
    new_tail = copy_ll[len(copy_ll) - real_places - 1]
    index = len(copy_ll) - 1
    for _ in range(real_places):
        copy_ll[index].next = head
        head = copy_ll[index]
        index -= 1
    new_tail.next = None
    return head

print(rotate_right(ll_a.head.next, places))

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

def rotate_right(head, k):
    if head is None:
        return None
    if head.next is None:
        return head
    old_tail = head
    length = 1
    while old_tail.next is not None:
        length += 1
        old_tail = old_tail.next
    old_tail.next = head
    new_tail = head
    for i in range(length - (k % length) - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''