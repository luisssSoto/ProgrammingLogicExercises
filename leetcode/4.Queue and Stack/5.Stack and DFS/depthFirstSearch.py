class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

def dfs(node, target):
    visited = set()
    visited.add(node)
    stack = [node]
    while stack:
        curr = stack[-1]
        if curr.val == target:
            return [curr, curr.val, curr.left, curr.right]
        if curr.left and curr.left not in visited:
            stack.append(curr.left)
            visited.add(curr.left)
            continue
        if curr.right and curr.right not in visited:
            stack.append(curr.right)
            visited.add(curr.right)
            continue
        stack.pop()
    return -1

# testcase
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

binary_tree = BinaryTree(node1)

print(dfs(binary_tree.root, 6))
