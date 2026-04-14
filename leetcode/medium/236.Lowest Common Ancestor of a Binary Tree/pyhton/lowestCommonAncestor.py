"""Lowest Common Ancestor of a Binary Tree"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.nodes = 0
        self.root = root

node3 = Node(3)
node5 = Node(5)
node1 = Node(1)
node6 = Node(6)
node2 = Node(2)
node0 = Node(0)
node8 = Node(8)
node7 = Node(7)
node4 = Node(4)

node3.left = node5
node3.right = node1

node5.left = node6
node5.right = node2

node1.left = node0
node1.right = node8

node2.left = node7
node2.right = node4

binary_tree = BinaryTree(node3)

def lowest_common_ancestor(root: Node, p: Node, q: Node) -> Node:
    if not root:
        return None
    if root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

def lowest_common_ancestor(root: Node, p: Node, q: Node) -> Node:
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        curr = stack.pop()
        if curr.left:
            stack.append(curr.left)
            parent[curr.left] = curr
        if curr.right:
            stack.append(curr.right)
            parent[curr.right] = curr
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent.get(p)
    while q not in ancestors:
        q = parent[q]
    return q

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

    

print(lowest_common_ancestor(node3, node6, node2))

