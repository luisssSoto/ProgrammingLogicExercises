"""Design a Linked List"""

class Node():
    """node"""
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList():
    def __init__(self):
        self.size = 0
        self.head = Node(0) # Sentinal node as a pseudo-head
    
    # get the value according the index if the index is invalid return -1
    def get(self, index : int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        # index steps needed to move from sentinal node until desire index
        for _ in range(index + 1):
            current = current.next
        print(current.val)
        return current.val
    
    # add a node at any index if is a valid one
    def addAtIndex(self, index : int, val : int) -> None:
        # if index is greater than the length, the node will not be added
        if index > self.size:
            return 
        # if the index is less than 0, the node will be added at the begining
        if index < 0:
            index = 0
        self.size += 1
        # find the predecessor of the node to be added
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next
        to_add = Node(val)
        to_add.next = predecessor.next
        predecessor.next = to_add
    
    # Add a node at head of the linked list
    def addAtHead(self, val : int) -> None:
        self.addAtIndex(0, val)

    # Append a node at the end of the linked list
    def addAtTail(self, val : int) -> None:
        self.addAtIndex(self.size, val)

    # Delete a node if the index is valid
    def deleteAtIndex(self, index : int) -> None:
        # Check if the index is valid
        if index < 0 or index >= self.size:
            return
        # Decrement the size of the linked list
        self.size -= 1
        # Find the predecessor
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next
        # Delete the node
        predecessor.next = predecessor.next.next
        print(predecessor.val)

# Testing

#Input:
test_data0 = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
test_data_01 = [[], [1], [3], [1, 2], [1], [1], [1]]
#Output:
#  [null, null, null, null, 2, null, 3]
obj = MyLinkedList()
obj.addAtHead(38)
obj.addAtTail(66)
obj.addAtTail(61)
obj.addAtTail(76)
obj.addAtTail(26)
obj.addAtTail(37)
obj.addAtTail(8)
obj.deleteAtIndex(5)
obj.addAtHead(4)
obj.addAtHead(45)
print(obj.get(4))

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

'''Complexity Analysis
Time complexity: O(1) for addAtHead. O(k) for get, addAtIndex, 
and deleteAtIndex, where k is an index of the element to get, add 
or delete. O(N) for addAtTail.
Space complexity: O(1) for all operations.'''