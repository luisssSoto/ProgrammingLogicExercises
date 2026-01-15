"""Maximum Depth of Binary Tree"""

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

def max_depth(root: TreeNode) -> int:
    '''Top-Down Iteratively'''
    if not root:
        return 0
    stack = [(root, 1)]
    max_depth = 0
    while stack:
        root, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if root.left:
            stack.append((root.left, depth + 1))
        if root.right:
            stack.append((root.right, depth + 1))
    return max_depth

def max_depth(root: TreeNode) -> int:
    '''Top-Down recursively'''
    def recursive(r, max_depth, depth):
        if not r:
            return max_depth
        max_depth = max(max_depth, depth)
        if r.left:
            max_depth = recursive(r.left, max_depth, depth + 1)
        if r.right:
            max_depth = recursive(r.right, max_depth, depth + 1)
        return max_depth
    maximum_depth = 0
    return recursive(root, maximum_depth, 1)

def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    stack = []
    depth = 0
    max_depth = 0
    while stack or root:
        while root:
            depth += 1
            stack.append((root, depth))
            root = root.left
        root, depth = stack.pop()
        if not root.left and not root.right:
            max_depth = max(max_depth, depth)
        if root.right:
            root = root.right
        else:
            root = None
    return max_depth

def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root, False)]  # (node, visited)
    depth = {}

    while stack:
        node, visited = stack.pop()

        if not node:
            continue

        if visited:
            # children already processed → compute depth
            left_depth = depth.get(node.left, 0)
            right_depth = depth.get(node.right, 0)
            depth[node] = 1 + max(left_depth, right_depth)
        else:
            # post-order: left → right → node
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return depth[root]


'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

node4 = TreeNode(4)
node5 = TreeNode(5)
node8 = TreeNode(8)

node2.left = node4
node2.right = node5
node3.right = node8

node6 = TreeNode(6)
node7 = TreeNode(7)
node9 = TreeNode(9)

node5.left = node6
node5.right = node7
node8.left = node9

binaryTree = BinaryTree(node1)

print(max_depth(binaryTree.root))



