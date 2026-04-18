"""297. Serialize and Deserialize Binary Tree"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
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
        while ser[-1] == "None,":
            ser.pop()
        print(f"ser: {ser}")
        print(len(ser))
        return "".join(ser)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(f"data: {data}")
        if data == "None":
            return []
        data = data.rstrip(',')
        data = data.split(",")
        des = []
        index = 0
        curr = TreeNode(data[index])
        des.append(curr)
        left = 1
        right = 2
        while left < len(data):
            curr = des[index]
            if data[left] != 'None':
                node = TreeNode(int(data[left]))
                des.append(node)
                curr.left = node
            else:
                curr.left = None
            if right < len(data):
                if data[right] != 'None':
                    node = TreeNode(int(data[right]))
                    des.append(node)
                    curr.right = node
                else:
                    curr.right = None
            index += 1
            left += 2
            right = left + 1
        return des[0]

    

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

ans = des.deserialize(ser.serialize(bt.root))
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