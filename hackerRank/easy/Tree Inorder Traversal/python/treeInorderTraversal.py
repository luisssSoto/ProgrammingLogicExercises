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
        current_node = self.root
        while True and current_node:
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

    def in_order_iterative(self, root):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            print(root.info, end=" ")
            root = root.right
        print()

    def in_order_recursive(self, root):
        def recursive(r):
            if not r:
                return 
            recursive(r.left)
            print(r.info, end=" ")
            recursive(r.right)
        recursive(root)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcases
t1 = [2,5,3,4,6]
my_root = TreeNode(1)
binary_tree = BinaryTree(my_root)
for node_val in t1:
    binary_tree.create(node_val)
binary_tree.in_order_iterative(my_root)
binary_tree.in_order_recursive(my_root)