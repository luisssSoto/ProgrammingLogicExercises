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
        def recursive(stack, result, previous_node, root):
            if not root and not stack:
                return
            elif root:
                stack.append(root)
                root = root.left
                recursive(stack, result, previous_node, root)
            else:
                root = stack[-1]
                if not root.right or root.right == previous_node:
                    result.append(root.val)
                    previous_node = stack.pop()
                    root = None
                    recursive(stack, result, previous_node, root)
                else:
                    root = root.right
                    recursive(stack, result, previous_node, root)
        s = []
        r = []
        pn = None
        cn = self.root
        recursive(s, r, pn, cn)
        return r

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