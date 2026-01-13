"""Symmetric Tree"""

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

def is_symmetric(root: BinaryTree[TreeNode]) -> bool:
    stack = []
    left_vals = []
    right_vals = []
    while stack or root:
        while root:
            stack.append(root)
            left_vals.append(root.val)
            root = root.left
        left_vals.append(root)
        root = stack.pop()
        if not stack:
            break
        if root.right:
            root = root.right
        else:
            root = None
    while stack or root:
        while root:
            stack.append(root)
            right_vals.append(root.val)
            root = root.right
        right_vals.append(root)
        root = stack.pop()
        if not stack:
            break
        if root.left:
            root = root.left
        else:
            root = None
    print(f"left vals: {left_vals}, right_vals: {right_vals}")
    return left_vals == right_vals

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

def is_symmetric(root: BinaryTree[TreeNode]) -> bool:
    queue = [root.left, root.right]
    while queue:
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        if not node_left and not node_right:
            continue
        if not node_left or not node_right:
            return False
        if node_left.val != node_right.val:
            return False
        queue.append(node_left.left)
        queue.append(node_right.right)
        queue.append(node_left.right)
        queue.append(node_right.left)
    return True

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''