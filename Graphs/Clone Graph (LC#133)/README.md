# Clone Graph 📊

## Problem Statement

Given a reference of a node in a **connected** undirected graph, return a **deep copy** (clone) of the graph. Each node in the graph contains a `val` (int) and a list (`List[Node]`) of its neighbors.

## Approach 🌟

To clone a graph, we can use a depth-first search (DFS) approach to traverse the original graph and create a copy of each node along with its neighbors. Here's how we can approach the problem:

1. Initialize an empty dictionary `visited` to store the mapping between original nodes and their corresponding clones.
2. Define a recursive function `clone(node)` to perform DFS traversal and clone the nodes and their neighbors.
3. If the current node is `None`, return `None`.
4. If the current node is already visited (i.e., present in the `visited` dictionary), return its clone.
5. Otherwise, create a new clone node with the same value as the current node, add it to the `visited` dictionary, and recursively clone its neighbors.
6. Return the clone of the current node.
7. Call the `clone(node)` function with the input node to start the DFS traversal and return the clone of the entire graph.

## Complexity Analysis ⚙️

- Time Complexity: O(V + E), where `V` is the number of vertices (nodes) in the graph and `E` is the number of edges in the graph.
  - The DFS traversal explores each node and each edge exactly once.
- Space Complexity: O(V), where `V` is the number of vertices (nodes) in the graph.
  - The space complexity includes the space required for the `visited` dictionary and the space required for the recursive call stack during DFS traversal.
