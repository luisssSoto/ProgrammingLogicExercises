"""Construct Binary Tree from Preorder and Inorder Traversal"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    def helper(l, r):
        if l > r:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = idx_map[val]
        root.left = helper(l, idx - 1)
        root.right = helper(idx + 1, r)
        return root
    idx_map = {val:idx for idx, val in enumerate(inorder)}
    print(idx_map)
    return helper(0, len(inorder) - 1)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcases
pre = [3,9,20,15,7]
ino = [9,3,15,20,7]

print(build_tree(pre, ino))