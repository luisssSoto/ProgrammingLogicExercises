"""Count Univalue Subtrees"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.nodes = 0
        self.root = root
        
def count_unival_subtrees(root: BinaryTree[TreeNode]) -> int:
    def dfs(node, count):
        if node is None:
            return True

        isLeftUniValue = dfs(node.left, count)
        isRightUniValue = dfs(node.right, count)

        # If both the children form uni-value subtrees, we compare the value of
        # chidrens node with the node value.
        if isLeftUniValue and isRightUniValue:
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False

            count[0] += 1
            return True
        # Else if any of the child does not form a uni-value subtree, the subtree
        # rooted at node cannot be a uni-value subtree.
        return False

    count = [0]
    dfs(root, count)
    return count[0]

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(N)'''

# tescases
t1 = [5,1,5,5,5,None,5]
root = TreeNode(t1[0])
node1 = TreeNode(t1[1])
node2 = TreeNode(t1[2])
node3 = TreeNode(t1[3])
node4 = TreeNode(t1[4])
node5 = TreeNode(t1[6])

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5

tree = BinaryTree(root)

print(count_unival_subtrees(tree.root))
