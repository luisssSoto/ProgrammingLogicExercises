"""Path Sum"""
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = []
        count = 0
        while stack or root:
            while root:
                count += root.val
                stack.append((root, count))
                root = root.left
            root, last_count = stack.pop()
            if root.right:
                root = root.right
            else:
                if not root.left and last_count == targetSum:
                    return True
                if stack:
                    count = stack[-1][1]
                root = None
        return False

def path_sum(root: TreeNode, targetSum: int ) -> bool:
    def recursive(r, current):
        if not r:
            return False
        current += r.val
        if not r.left and not r.right:
            return current == targetSum       
        return recursive(r.left, current) or recursive(r.right, current)
    return recursive(root, 0)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# testcase
node5 = TreeNode(5)
node4_left = TreeNode(4)
node8 = TreeNode(8)

node5.left = node4_left
node5.right = node8

node11 = TreeNode(11)
node13 = TreeNode(13)
node4_right = TreeNode(4)

node4_left.left = node11
node8.left = node13
node8.right = node4_right

node7 = TreeNode(7)
node2 = TreeNode(2)

node11.left = node7
node11.right = node2

binary_tree = BinaryTree(node5)
target_sum = 22
print(path_sum(binary_tree.root, target_sum))