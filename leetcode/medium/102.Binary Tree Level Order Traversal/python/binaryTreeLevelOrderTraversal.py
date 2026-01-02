"""Binary Tree Level Order Traversal"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.nodes = 0
        self.root = root

def level_order_iterative(root) -> list[list[int]]:
    levels = []
    if not root:
        return levels
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            root = queue.pop(0)
            level.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        levels.append(level)
    return levels

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

def level_order_recursive(root) -> list[list[int]]:
    levels = []
    if not root:
        return levels
    def recursive(r, level):
        if len(levels) == level:
            levels.append([])
        levels[level].append(r.val)
        if r.left:
            recursive(r.left, level + 1)
        if r.right:
            recursive(r.right, level + 1)
    recursive(root, 0)
    return levels

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# testcase 1
root = TreeNode(3)
binary_tree = BinaryTree(root)
left_second_level = TreeNode(9)
root.left = left_second_level
right_second_level = TreeNode(20)
root.right = right_second_level
left_third_level = TreeNode(15)
right_third_level = TreeNode(7)
right_second_level.left = left_third_level
right_second_level.right = right_third_level

print(level_order_iterative(root))
print(level_order_recursive(root))