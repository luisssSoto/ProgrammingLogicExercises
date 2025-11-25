"""Preorder Traversal"""

class TreeNode:
    def __init__(self, info):
        self.left = None
        self.info = info
        self.right = None
    
    def __str__(self):
        return str(self.info)
    
class BinaryTree:
    def __init__(self, root):
        self.root = root

    def create(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            current_node = self.root
        while True:
            if val < current_node.info:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = TreeNode(val)
                    break
            elif val > current_node.info:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = TreeNode(val)
                    break
            else:
                break
    
    def preorder_traversal_iterative(self):
        if not self.root:
            return None
        current_node = self.root
        stack = [current_node]
        while stack:
            current_node = stack.pop()
            # result: 
            print(current_node.info, end=" ")
            if current_node:
                if current_node.right:
                    stack.append(current_node.right)
                if current_node.left:
                    stack.append(current_node.left)
        print()
    
    def preorder_traversal_recursive(self):
        def recursive(root):
            if not root:
                return
            print(root.info, end=" ")
            recursive(root.left)
            recursive(root.right)
        current_node = self.root
        recursive(current_node)
        print()

# Prepare data
nodes_vals = [2,5,3,4,6]
root = TreeNode(1)
my_binary_tree = BinaryTree(root)
for val in nodes_vals:
    my_binary_tree.create(val)
my_binary_tree.preorder_traversal_recursive()
my_binary_tree.preorder_traversal_iterative()

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''