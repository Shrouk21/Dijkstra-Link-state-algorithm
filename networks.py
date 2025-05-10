import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import dijkstra

def create_graph_from_input():
    """
    Create a graph from user input.
    The first line contains the number of nodes (n) and edges (m).
    Each of the next m lines contains src_node, dest_node, weight.
    """
    n, m = map(int, input("Enter number of nodes and edges (n m): ").split())
    G = nx.Graph()
    print("Enter edges in the format: src_node dest_node weight")
    for _ in range(m):
        src, dest, weight = input().split()
        weight = int(weight)
        G.add_edge(src, dest, weight=weight)
    return G

def draw_graph(G):
    """
    Draw the graph using matplotlib.
    """
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Graph Visualization")
    plt.axis('off')
    plt.show()

def compute_forwarding_table(graph, source):
    """
    Compute the forwarding table for a given source node using Dijkstra's algorithm.
    """
    forwarding_table = {}
    _, previous_nodes = dijkstra(graph, source) 
    
    for destination in graph.nodes():
        if destination != source:
            current = destination
            while previous_nodes[current] != source:
                current = previous_nodes[current]
            forwarding_table[destination] = (source, current)
    return forwarding_table

def print_forwarding_table(node, table):
    """
    Print the forwarding table for a given node.
    """
    print(f"Forwarding Table for {node}:")
    print(f"{'Destination':<12}{'Link':<12}")
    for dest, link in table.items():
        print(f"{dest:<12}{link}")

def main():
    # Step 1: Create the graph from user input
    G = create_graph_from_input()

    # Step 2: Visualize the original topology
    draw_graph(G)

    # Step 3: Compute and print forwarding tables for all nodes
    for node in G.nodes():
        table = compute_forwarding_table(G, node)
        print_forwarding_table(node, table)

if __name__ == "__main__":
    main()