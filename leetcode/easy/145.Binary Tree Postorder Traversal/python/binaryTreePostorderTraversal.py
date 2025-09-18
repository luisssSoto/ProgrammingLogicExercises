"""Binary Tree Postorder Traversal"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root):
    result = []

    # If the root is null, return an empty list
    if root is None:
        return result

    # To keep track of the previously processed node
    previous_node = None
    # Stack to manage the traversal
    traversal_stack = []

    # Process nodes until both the root is null and the stack is empty
    while root is not None or len(traversal_stack) > 0:
        # Traverse to the leftmost node
        if root is not None:
            traversal_stack.append(root)
            root = root.left
        else:
            # Peek at the top node of the stack
            root = traversal_stack[-1]

            # If there is no right child or the right child was already processed
            if root.right is None or root.right == previous_node:
                result.append(root.val)
                traversal_stack.pop()
                previous_node = root
                root = None  # Ensure we don’t traverse again from this node
            else:
                # Move to the right child
                root = root.right

    return result

left = TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5, left=TreeNode(val=6), right=TreeNode(val=7)))
right = TreeNode(val=3, left=None, right=TreeNode(val=8, left=TreeNode(val=9), right=TreeNode(val=10)))
root = TreeNode(val=1, left=left, right=right)
print(postorder_traversal(root))