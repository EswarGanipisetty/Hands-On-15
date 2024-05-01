import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    # The distance from start node to itself is 0
    distances[start] = 0
    # Priority queue to hold nodes to be visited, initially with start node
    queue = [(0, start)]

    while queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(queue)

        # If current distance is greater than the known shortest distance, skip
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If this path is shorter than the previously known shortest path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add neighbor to the priority queue to explore its neighbors later
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'
print(dijkstra(graph, start_node))
