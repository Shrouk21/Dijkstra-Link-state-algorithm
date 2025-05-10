# Dijkstra Link-State Algorithm

This project implements the Dijkstra Link-State Algorithm to compute the shortest paths and generate forwarding tables in a network graph. It uses Python’s `networkx` library for graph representation and `matplotlib` for visualization.

## Features

* Create a graph from user input
* Visualize the graph topology
* Compute shortest paths using Dijkstra's algorithm
* Generate and display forwarding tables for all nodes

## Requirements

* Python 3.x
* `networkx`
* `matplotlib`

## Usage

1. Run the program:

   ```bash
   python networks.py
   ```

2. Follow the prompts to input the number of nodes, edges, and their weights.

3. View the resulting graph visualization and forwarding tables.

## File Structure

* `dijkstra.py` — Implements Dijkstra's algorithm
* `networks.py` — Main script for graph creation, visualization, and forwarding table computation

## Example

**Input:**

```
Enter number of nodes and edges (n m): 4 5  
Enter edges in the format: src_node dest_node weight  
A B 1  
A C 4  
B C 2  
B D 6  
C D 3  
```

**Output:**

* Graph visualization displayed using `matplotlib`
* Forwarding tables printed for each node


