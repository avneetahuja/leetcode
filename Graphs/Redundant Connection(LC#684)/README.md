# Find Redundant Connection 🌐

## Problem Statement

Given a list of edges `edges` representing an undirected graph, where `edges[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi`, find and return the edge that, when removed, would result in the graph being disconnected.

If multiple answers exist, return the one with the smallest index. If there are no such edges that can be removed to make the graph disconnected, return an empty array.

## Approach 🌟

To find the redundant connection in the graph, we can use the Union-Find (Disjoint Set Union) algorithm. We iterate through each edge and perform the following steps:

1. Initialize a disjoint set data structure with each node as its own parent and rank array to track the height of each tree.
2. For each edge `[u, v]`, find the parent (representative) of both nodes `u` and `v`.
3. If both nodes have the same parent, it means they are already connected, and adding this edge will create a cycle. In this case, this edge is redundant, and we return it.
4. If they have different parents, we union the sets by making one the parent of the other.
5. Repeat this process for all edges until we find the redundant connection or iterate through all edges.

## Complexity Analysis ⚙️

- Time Complexity: O(N * α(N)), where `N` is the number of vertices (nodes) and α is the inverse Ackermann function.
  - The union-find operations have an almost constant time complexity due to the path compression and union by rank optimizations.
- Space Complexity: O(N), where `N` is the number of vertices (nodes) in the graph.
  - The space complexity is mainly determined by the space required for the parent and rank arrays in the disjoint set data structure.
