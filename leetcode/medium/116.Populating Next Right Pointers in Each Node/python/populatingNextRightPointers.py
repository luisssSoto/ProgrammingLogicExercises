"""Populating Next Right Pointers"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Tree:
    def __init__(self, root: Node):
        self.root = root

def connect(root: Tree[Node]) -> Tree[Node]:
    if not root:
        return root
    from collections import deque
    queue = deque()
    queue.append(root)
    while queue:
        length = len(queue)
        for i in range(length):
            curr = queue.popleft()
            if i + 1 == length:
                curr.next = None
            else:
                curr.next = queue[0]
            if curr.left and curr.left:
                queue.append(curr.left)
            if curr.right and curr.right: 
                queue.append(curr.right)
    return root
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

def connect(root: Tree[Node]) -> Tree[Node]:
        if not root:
            return root
        left_most = root
        while left_most.left:
            head = left_most
            while head:
                if head.left:
                    head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left_most = left_most.left
        return root
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''