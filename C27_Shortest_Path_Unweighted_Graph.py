from collections import deque

def Shortest_Path_Unweighted_Graph(V, edges, start, end):
    graph = {i: [] for i in range(V)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    queue = deque([start])
    visited = {start: 0}

    while queue:
        node = queue.popleft()  
        if node == end:
            return visited[node]  

        for neighbor in graph[node]:
            if neighbor not in visited:  
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)

    return -1

# Test case 1
V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start = 0
end = 4
print(Shortest_Path_Unweighted_Graph(V, edges, start, end))

# Test case 2
V = 3
edges = [[0, 1], [1, 2]]
start = 0
end = 2
print(Shortest_Path_Unweighted_Graph(V, edges, start, end))

# Test case 3
V = 4
edges =  [[0, 1], [1, 2]]
start = 2
end = 3
print(Shortest_Path_Unweighted_Graph(V, edges, start, end))