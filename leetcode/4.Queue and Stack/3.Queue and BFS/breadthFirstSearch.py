"""Breadth First Search (BFS)"""

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root


def bfs(root: TreeNode, target) -> int:
    """Find the shortest path to get the target node"""
    queue = []
    queue.append(root)
    # add a set if you desiree to put attention to the visited nodes
    visited_nodes = set() 
    visited_nodes.add(root)
    step = 0
    while queue:
        queue_len = len(queue)
        for i in range(queue_len):
            node = queue.pop(0)
            if node.val == target:
                return step
            else:
                # keep track of the visited nodes could help us to don't get stuck
                # if we are handling a graph with cycle
                if node.left and node.left not in visited_nodes:
                    queue.append(node.left)
                    visited_nodes.add(node.left)
                if node.right and node.right not in visited_nodes:
                    queue.append(node.right)
                    visited_nodes.add(node.right)
        step += 1
    return f'The target: {target} wasn\'t found'

# 1. testcase
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

node4 = TreeNode(4)
node5 = TreeNode(5)
node8 = TreeNode(8)

node2.left = node4
node2.right = node5
node3.right = node8

node6 = TreeNode(6)
node7 = TreeNode(7)
node9 = TreeNode(9)

node5.left = node6
node5.right = node7
node8.left = node9

binaryTree = BinaryTree(node1)
targ = 1
print(bfs(binaryTree.root, targ))