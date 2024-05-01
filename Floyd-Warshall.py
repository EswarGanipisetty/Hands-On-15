INF = float('inf')

def floyd_warshall(graph):
    # Number of vertices
    V = len(graph)
    
    # Initialize the distance matrix with the given graph
    dist = [[INF] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif (i, j) in graph:
                dist[i][j] = graph[(i, j)]
    
    # Apply the Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example usage
graph = {
    (0, 1): 3,
    (0, 2): 6,
    (1, 0): 3,
    (1, 2): 2,
    (2, 0): 6,
    (2, 1): 2,
}
result = floyd_warshall(graph)
for row in result:
    print(row)
