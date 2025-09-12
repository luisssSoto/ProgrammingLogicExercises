"""Binary Tree Inorder Traversal"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

values = [1,None,2,3]
my_tree_node = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3)))
print(inorder_traversal(my_tree_node))