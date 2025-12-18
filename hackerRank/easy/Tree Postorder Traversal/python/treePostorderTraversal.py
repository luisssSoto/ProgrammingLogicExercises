"""Tree Postorder Traversal"""
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

    def post_order_iterative(self, root):
        previous_node = None
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if not root.right or root.right == previous_node:
                    print(root.info, end=" ")
                    previous_node = stack.pop()
                    root = None
                else:
                    root = root.right

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcases
t1 = [3,6,5,2,1]
my_root = TreeNode(4)
binary_tree = BinaryTree(my_root)
for node_val in t1:
    binary_tree.create(node_val)
binary_tree.post_order_iterative(my_root)
