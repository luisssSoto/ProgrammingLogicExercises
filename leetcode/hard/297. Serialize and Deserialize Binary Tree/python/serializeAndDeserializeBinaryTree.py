"""297. Serialize and Deserialize Binary Tree"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

# Approach 1: BFS 
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        BFS
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        queue = deque()
        queue.append(root)
        ser = [str(root.val) + ","]
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    ser.append(str(curr.left.val) + ",")
                else:
                    ser.append("None,")
                if curr.right:
                    queue.append(curr.right)
                    ser.append(str(curr.right.val) + ",")
                else:
                    ser.append("None,")
        return "".join(ser)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        BFS
        :type data: str
        :rtype: TreeNode
        """
        print(f"data: {data}")
        if data == "None":
            return []
        data = data.rstrip(',')
        data = data.split(",")
        data = deque(data)
        des = []
        index = 0
        curr = TreeNode(int(data.popleft()))
        des.append(curr)
        while data:
            curr = des[index]
            if data[0] != 'None':
                node = TreeNode(int(data.popleft()))
                des.append(node)
                curr.left = node
            else:
                data.popleft()
                curr.left = None
            if len(data) > 0:
                if data[0] != 'None':
                    node = TreeNode(int(data.popleft()))
                    des.append(node)
                    curr.right = node
                else:
                    data.popleft()
                    curr.right = None
            index += 1
        return des[0]

'''Complexity Analysis: 
Space Complexity: O(N)
Time Complexity: O(N)'''

# Approach 2: DFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        DFS
        :type root: TreeNode
        :rtype: str
        """
        def rhelper(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = rhelper(root.left, string)
                string = rhelper(root.right, string)
            return string
        return rhelper(root, '')
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        BFS
        :type data: str
        :rtype: TreeNode
        """
        def rhelper(l):
            if l[0] == "None":
                l.popleft()
                return None
            root = TreeNode(l.popleft())
            root.left = rhelper(l)
            root.right = rhelper(l)
            return root
        data = data.split(",")
        data = deque(data)
        root = rhelper(data)
        return root

'''Complexity Analysis: 
Space Complexity: O(N)
Time Complexity: O(N)'''

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

bt = BinaryTree(node1)
c = Codec()

ser = Codec()
des = Codec()

s = ser.serialize(bt.root)
print(s)

ans = des.deserialize(s)
print(ans)

a = ser.serialize(None)
print(a)

[1,2]
node1 = TreeNode(1)
node2 = TreeNode(2)
node1.left = node2

s = ser.serialize(node1)
print(s)
d = des.deserialize(s)