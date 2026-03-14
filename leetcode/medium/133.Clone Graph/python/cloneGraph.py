from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return node
    elif not node.neighbors:
        clone_graph = Node(1, None)
        return clone_graph
    elif node:
        stack = [node]
        visited_vals = {}
        clone_graph = []
        while stack:
            curr_node = stack.pop()
            if curr_node.val not in visited_vals:
                new_node = Node(curr_node.val)
                visited_vals[new_node.val] = new_node
            else:
                new_node = visited_vals[curr_node.val]
            clone_graph.append(new_node)
            for nd in curr_node.neighbors:
                if nd.val not in visited_vals:
                    stack.append(nd)
                    neighbor = Node(nd.val)
                    visited_vals[neighbor.val] = neighbor
                else:
                    neighbor = visited_vals[nd.val]
                new_node.neighbors.append(neighbor)   
        return clone_graph[0]

def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """DFS Approach"""
    if not node:
        return node
    stack = [node]
    copy_node = Node(node.val)
    visited = {node: copy_node}
    while stack:
        nd = stack.pop()
        for neighbor in nd.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                visited[neighbor] = Node(neighbor.val)
            visited[nd].neighbors.append(visited[neighbor])
    return copy_node

def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """BFS Approach"""
    from collections import deque
    if not node:
        return node
    queue = deque([node])
    visited = {node: Node(node.val)}
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            visited[curr].neighbors.append(visited[neighbor])
    return visited[node]
        
# testcase
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
t1 = [[node2,node4],[node1,node3],[node2,node4],[node1,node3]]
node1.neighbors = t1[0]
node2.neighbors = t1[1]
node3.neighbors = t1[2]
node4.neighbors = t1[3]

print(cloneGraph(node1))
print(clone_graph(node1))