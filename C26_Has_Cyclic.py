def Has_Cycle(v, parent, graph, visited):
    visited.add(v)
    
    for neighbor in graph[v]:
        if neighbor not in visited:
            if Has_Cycle(neighbor, v, graph, visited):
                return True
        elif parent != neighbor:
            return True
            
    return False

def Detect_Cycle_in_Undirected_Graph(V, edges):
    graph = {i: [] for i in range(V)}
    
    # Building the adjacency list
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    
    for i in range(V):
        if i not in visited:
            if Has_Cycle(i, -1, graph, visited):
                return True
    
    return False

# Test Case 1
V = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
print(Detect_Cycle_in_Undirected_Graph(V, edges))

# Test Case 1
V = 3
edges =  [[0, 1], [1, 2]]
print(Detect_Cycle_in_Undirected_Graph(V, edges))

# Test Case 1
V = 1
edges = []
print(Detect_Cycle_in_Undirected_Graph(V, edges))

# Test Case 1
V = 4
edges = [[0, 1], [1, 2], [2, 3]]
print(Detect_Cycle_in_Undirected_Graph(V, edges))
