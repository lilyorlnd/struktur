graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []

def dfs(graph, start, visited):
    visited.append(start) 
    print(start, end=' ')
    
    for neighbour in graph[start]: 
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

dfs(graph, 'A', visited)
