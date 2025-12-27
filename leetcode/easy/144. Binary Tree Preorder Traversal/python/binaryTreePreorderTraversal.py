"""Binary Tree Pre Order Traversal"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def create(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            current_node = self.root
            while True:
                if val < current_node.val:
                    if self.root.left:
                        current_node = self.root
                    else:
                        self.root.left = TreeNode(val)
                        break
                elif val > current_node.val:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = TreeNode(val)
                        break
                else:
                    break

# Approach 1. 
def preorderTraversal(root):
    if root is None:
        return []
    stack = [root]
    output = []
    while len(stack) > 0:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
    return output

# Approach 2. Iterative
def preorderTraversal(root: BinaryTree[TreeNode]) -> list[int]:
        if not root:
            return []
        stack = []
        nodes_values = []
        current_node = root
        while stack or current_node:
            while current_node:
                nodes_values.append(current_node.val)
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            if current_node.right:
                current_node = current_node.right
            else:
                current_node = None
        return nodes_values

# Approach 3. Recursive
def preorderTraversal(root: BinaryTree[TreeNode]) -> list[int]:
    def recursive(res, root):
        if not root:
            return
        res.append(root.val)
        recursive(res, root.left)
        recursive(res, root.right)
    nodes_values = []
    recursive(nodes_values, root)
    return nodes_values
