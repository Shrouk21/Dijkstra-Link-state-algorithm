from heapq import heappop, heappush

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest path from start to all other nodes.
    """
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes()}
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def shortest_path(graph, start, end):
    """
    Find the shortest path from start to end using Dijkstra's algorithm.
    """
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    current_node = end
    
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    
    path.reverse()
    return path, distances[end]