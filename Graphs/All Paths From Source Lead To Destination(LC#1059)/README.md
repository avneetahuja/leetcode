# Leads to Destination 🚀

## Problem Statement

Given the integer `n`, an array `edges` where `edges[i] = [fromi, toi]` represents a directed edge from node `fromi` to node `toi`, and two integers `source` and `destination`, determine whether all paths from `source` lead to `destination`.

You must return `true` if every node in the graph is either the destination or it has exactly one outgoing edge to another node in the graph; otherwise, return `false`.

## Approach 🌟

To determine whether all paths from the source lead to the destination, we can use a depth-first search (DFS) approach to traverse the graph and check for the following conditions:

1. If the destination node has any outgoing edges, return `false` because it should be a sink node (i.e., no outgoing edges).
2. Perform DFS traversal from the source node to check if all paths lead to the destination.
3. Keep track of visited nodes to avoid infinite loops (cycles).
4. During DFS traversal, if we encounter a node with no outgoing edges, it should be the destination node.
5. If all paths from the source lead to the destination, return `true`; otherwise, return `false`.

## Complexity Analysis ⚙️

- Time Complexity: O(V + E), where `V` is the number of vertices (nodes) and `E` is the number of edges in the graph.
  - The DFS traversal explores each node and each edge exactly once.
- Space Complexity: O(V), where `V` is the number of vertices (nodes) in the graph.
  - The space complexity includes the space required for the graph representation and the space required for the recursive call stack during DFS traversal.
