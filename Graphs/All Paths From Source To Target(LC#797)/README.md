# All Paths from Source to Target 🛤️

## Problem Statement

You are given a directed acyclic graph (DAG) represented by its adjacency list `graph`, where `graph[i]` is a list of nodes connected to node `i`. Find all possible paths from node `0` to node `n - 1`, where `n` is the number of nodes in the graph. 

Return a list of all possible paths. You may return the answer in any order.

## Approach 🌟

To find all possible paths from the source node `0` to the target node `n - 1` in a directed acyclic graph (DAG), we can use a depth-first search (DFS) approach. Here's how we can approach the problem:

1. Initialize an empty list `res` to store all possible paths from `0` to `n - 1`.
2. Define a recursive function `search(node, path)` to perform DFS traversal from the current node `node` with the current path `path`.
3. If the current node is the target node `n - 1`, append the current path to `res` and return.
4. Otherwise, iterate through the neighbors of the current node `node` obtained from `graph[node]`. For each neighbor `neighbour`, recursively call `search(neighbour, path + [node])` to explore further.
5. Call the `search(0, [])` function to start the DFS traversal from the source node `0` with an empty path.
6. Return the list `res` containing all possible paths from `0` to `n - 1`.

## Complexity Analysis ⚙️

- Time Complexity: O(V + E), where `V` is the number of vertices (nodes) in the graph and `E` is the number of edges in the graph. 
  - The DFS traversal explores each vertex and each edge exactly once.
- Space Complexity: O(V + E)
  - The space complexity includes the space required for the adjacency list `graph`, the space required for the recursive call stack during DFS traversal, and the space required to store the resulting paths.
