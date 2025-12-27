class TreeNode:
    def __init__(self, info):
        self.left = None
        self.info = info
        self.right = None
    
    def __str__(self):
        return str(self.info)

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def create(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            current_node = self.root
            while True:
                if val < current_node.info:
                    if self.root.left:
                        current_node = self.root
                    else:
                        self.root.left = TreeNode(val)
                        break
                elif val > current_node.info:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = TreeNode(val)
                        break
                else:
                    break
    
    def pre_order_traversal_iterative(self):
        if not self.root:
            return []
        stack = []
        nodes_values = []
        current_node = self.root
        while stack or current_node:
            while current_node:
                nodes_values.append(current_node.info)
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            if current_node.right:
                current_node = current_node.right
            else:
                current_node = None
        return nodes_values
    
    def pre_order_traversal_recurive(self):
        def recursive(res, root):
            if not root:
                return
            res.append(root.info)
            recursive(res, root.left)
            recursive(res, root.right)
        nodes_values = []
        recursive(nodes_values, self.root)
        return nodes_values
    
    def inorder_traversal_iterative(self):
        if not self.root:
            return []
        stack = []
        nodes_values = []
        current_node = self.root
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            nodes_values.append(current_node.info)
            current_node = current_node.right
        return nodes_values
    
    def inorder_traversal_recursive(self):
        def recursive(res, root):
            if not root:
                return 
            recursive(res, root.left)
            res.append(root.info)
            recursive(res, root.right)
        nodes_values = []
        recursive(nodes_values, self.root)
        return nodes_values

    def post_order_traversal_iterative(self):
        if not self.root:
            return []
        stack = []
        nodes_values = []
        previous_node = None
        current_node = self.root
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack[-1]
            if not current_node.right or current_node.right == previous_node:
                previous_node = stack.pop()
                nodes_values.append(previous_node.info)
                current_node = None
            else:
                current_node = current_node.right
        return nodes_values
    
    def post_order_traversal_recursive(self):
        def recursive(res, root):
            if not root:
                return
            recursive(res, root.left)
            recursive(res, root.right)
            res.append(root.info)
        node_values = []
        recursive(node_values, self.root)
        return node_values
        
# testcases
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
print(binary_tree.pre_order_traversal_iterative())
print(binary_tree.pre_order_traversal_recurive())
print(binary_tree.inorder_traversal_iterative())
print(binary_tree.inorder_traversal_recursive())
print(binary_tree.post_order_traversal_iterative())
print(binary_tree.post_order_traversal_recursive())

binary_tree1 = BinaryTree(TreeNode(1))
for i in range(2, 10):
    binary_tree1.create(i)

