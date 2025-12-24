"""Tree Postorder Traversal"""
class TreeNode:
    def __init__(self, info):
        self.left = None
        self.info = info
        self.right = None

    def __str__(self):
        return str(self.info)

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def create(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(val)
                        break
                else:
                    break

    def post_order_iterative(self):
        root = self.root
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
    
    def post_order_recursive(self):
        def recursive(stack, root):
            if not root:
                return
            recursive(stack, root.left)
            recursive(stack, root.right)
            print(root.info, end=" ")
        s = []
        recursive(s, self.root)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcases
t1 = [3,6,5,2,1]
my_root = TreeNode(4)
binary_tree = BinaryTree()
for node_val in t1:
    binary_tree.create(node_val)
binary_tree.post_order_iterative()

import os
print(os.listdir())
root = TreeNode(1)
binary_tree1 = BinaryTree()

with open("./leetcode/testcase.txt", "r") as file:
    # nums = list(map(int, filter(lambda x: x.isdigit(), file.read())))
    # nums = [int(x) for x in file.read() if x.isdigit()]
    nums = file.read()
    print(nums)
    nums = nums.split()
    print(nums)
    print(len(nums))
    for val in nums:
        binary_tree1.create(int(val))
binary_tree1.post_order_iterative()
binary_tree1.post_order_recursive()