"""Binary Tree Postorder Traversal"""

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
def postorder_traversal(root):
    result = []
    if root is None:
        return result
    previous_node = None
    traversal_stack = []
    while root is not None or len(traversal_stack) > 0:
        if root is not None:
            traversal_stack.append(root)
            root = root.left
        else:
            root = traversal_stack[-1]
            if root.right is None or root.right == previous_node:
                result.append(root.val)
                traversal_stack.pop()
                previous_node = root
                root = None
            else:
                root = root.right
    return result

# Approach 2. Iterative
def postorderTraversal(root: BinaryTree[TreeNode]) -> list[int]:
    if not root:
        return []
    stack = []
    nodes_values = []
    previous_node = None
    current_node = root
    while stack or current_node:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack[-1]
        if not current_node.right or current_node.right == previous_node:
            previous_node = stack.pop()
            nodes_values.append(previous_node.val)
            current_node = None
        else:
            current_node = current_node.right
    return nodes_values

# Approach 3. Recursive
def postorderTraversal(root: BinaryTree[TreeNode]) -> list[int]:
    def recursive(res, root):
        if not root:
            return
        recursive(res, root.left)
        recursive(res, root.right)
        res.append(root.val)
    node_values = []
    recursive(node_values, root)
    return node_values

left = TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5, left=TreeNode(val=6), right=TreeNode(val=7)))
right = TreeNode(val=3, left=None, right=TreeNode(val=8, left=TreeNode(val=9), right=TreeNode(val=10)))
root = TreeNode(val=1, left=left, right=right)
print(postorder_traversal(root))