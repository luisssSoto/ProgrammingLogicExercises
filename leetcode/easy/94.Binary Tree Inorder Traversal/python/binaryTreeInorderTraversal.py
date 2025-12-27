"""Binary Tree Inorder Traversal"""

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
def inorder_traversal(root):
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

# Approach 2. Iterative
def inorderTraversal(root: BinaryTree[TreeNode]) -> list[int]:
        if not root:
            return []
        stack = []
        nodes_values = []
        current_node = root
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            nodes_values.append(current_node.val)
            current_node = current_node.right
        return nodes_values

# Approach 3. Recursive
def inorderTraversal(root: BinaryTree[TreeNode]) -> list[int]:
    def recursive(res, root):
        if not root:
            return 
        recursive(res, root.left)
        res.append(root.val)
        recursive(res, root.right)
    nodes_values = []
    recursive(nodes_values, root)
    return nodes_values


values = [1,None,2,3]
my_tree_node = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3)))
print(inorder_traversal(my_tree_node))