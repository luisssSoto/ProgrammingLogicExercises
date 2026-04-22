"""106. Construct Binary Tree from Inorder and Postorder Traversal"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode:
    def helper(l, r):
        if l > r:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        idx = idx_map[val]
        root.right = helper(idx + 1, r)
        root.left = helper(l, idx - 1)
        return root
    idx_map = {val: i for i, val in enumerate(inorder)}
    return helper(0, len(inorder) - 1)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# Testcases
i1 = [9,3,15,20,7]
p1 = [9,15,7,20,3]

print(build_tree(i1, p1))
