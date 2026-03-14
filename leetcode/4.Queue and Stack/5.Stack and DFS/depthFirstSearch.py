class Node:
    def __init__(self, val, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def iterative_dfs(node, target):
    """DFS Iterative"""
    stack = [node]
    visited = {node}
    while stack:
        node = stack.pop()
        if node.val == target:
            return node
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return -1

def recursive_dfs(node, target, visited):
    """DFS recursive"""
    if node.val == target:
        return True
    for neighbor in node.neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            if recursive_dfs(neighbor, target, visited) == True:
                return True
    return False    


# Modifying the functions to get the shortest distance to target
def shortest_path_ite_dfs(node, target):
    """iterative DFS"""
    stack = [(node, 0)]
    best = {node: 0}
    shortest = float('inf')
    while stack:
        nd, dis = stack.pop()
        if dis >= shortest:
            continue
        if nd.val == target:
            shortest = min(shortest, dis)
            continue
        for neighbor in nd.neighbors:
            new_dis = dis + 1
            if neighbor not in best or new_dis < best[neighbor]:
                best[neighbor] = new_dis
                stack.append((neighbor, new_dis))
    return shortest if shortest != float('inf') else - 1

# testcase
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')
node_g = Node('G')

node_a.neighbors = [node_b, node_c, node_d]
node_b.neighbors = [node_e]
node_c.neighbors = [node_e, node_f]
node_d.neighbors = [node_g]
node_f.neighbors = [node_g]

print(iterative_dfs(node_a, 'G'))
print(recursive_dfs(node_a, 'G', set()))
print(shortest_path_ite_dfs(node_a, 'G'))