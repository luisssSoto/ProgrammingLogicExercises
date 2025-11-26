"""Pre-Order Traversal"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.nodes = 0
        self.root = root
    def pre_order_traversal_recursive(self):
        '''Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(N)'''
        def recursive(root, ans):
            if not root:
                return 
            ans.append(root.val)
            recursive(root.left, ans)
            recursive(root.right, ans)
        current_node = self.root
        tree_nodes_val = []
        recursive(current_node, tree_nodes_val)
        return tree_nodes_val
    def inorder_traversal_recursive(self):
        '''Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(N)'''
        def recursive(root, ans):
            if not root:
                return
            recursive(root.left, ans)
            ans.append(root.val)
            recursive(root.right, ans)
        tree_nodes_val = []
        current_node = self.root
        recursive(current_node, tree_nodes_val)
        return tree_nodes_val
    
    def post_order_traversal_recursive(self):
        tree_nodes_val = []
        if self.root is None:
            return tree_nodes_val
        previous_node = None
        traversal_stack = []
        while self.root is not None or len(traversal_stack) > 0:
            if self.root is not None:
                traversal_stack.append(self.root)
                self.root = self.root.left
            else:
                self.root = traversal_stack[-1]
                if self.root.right is None or self.root.right == previous_node:
                    tree_nodes_val.append(self.root.val)
                    traversal_stack.pop()
                    previous_node = self.root
                    self.root = None
                else:
                    self.root = self.root.right
        return tree_nodes_val


node_f = TreeNode("F")
node_b = TreeNode("B")
node_a = TreeNode("A")
node_d = TreeNode("D")
node_c = TreeNode("C")
node_e = TreeNode("E")
node_g = TreeNode("G")
node_i = TreeNode("I")
node_h = TreeNode("H")

node_f.left = node_b
node_f.right = node_g
node_b.left = node_a
node_b.right = node_d
node_g.right = node_i
node_d.left = node_c
node_d.right = node_e
node_i.left = node_h

binary_tree = BinaryTree(node_f)

print(binary_tree)
print(binary_tree.pre_order_traversal_recursive())
print(binary_tree.inorder_traversal_recursive())
print(binary_tree.post_order_traversal_recursive())