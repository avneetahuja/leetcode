# Valid Path 🛤️

## Problem Statement

You are given an integer `n` representing the number of nodes in a graph and a list of edges `edges` where `edges[i] = [ui, vi]` indicates that there is an undirected edge between nodes `ui` and `vi`. You are also given integers `source` and `destination` representing the indices of the nodes you start and end at.

The graph is valid if there is a path between `source` and `destination`. Return `true` if the graph is valid, otherwise return `false`.

## Approach 🌟

To determine whether there is a valid path between the source and destination nodes, we can use the Union-Find algorithm. Here's how we can approach the problem:

1. Initialize a `root` array of size `n` and a `rank` array of size `n`, where `n` is the number of nodes in the graph. The `root[i]` represents the parent of node `i`, initially set to `i`. The `rank[i]` represents the rank (depth) of the subtree rooted at node `i`, initially set to `1`.
2. Define a function `find(i)` to find the root of the component containing node `i`. If `root[i]` is not equal to `i`, recursively find the root of the component containing the parent of node `i`. Apply path compression during the find operation.
3. Define a function `union(i, j)` to union the components containing nodes `i` and `j`. If the roots of `i` and `j` are not the same, merge the smaller rank tree into the larger rank tree. If the ranks are equal, choose any tree and increment its rank.
4. Check if the source and destination nodes are connected by calling the `connected(source, destination)` function, which returns `true` if the roots of the source and destination nodes are the same, indicating they belong to the same connected component.
5. Return `true` if the source and destination nodes are connected; otherwise, return `false`.

## Complexity Analysis ⚙️

- Time Complexity: O(nα(n) + m), where `n` is the number of nodes, `m` is the number of edges, and `α(n)` is the inverse Ackermann function.
  - Building the Union-Find data structure takes nearly constant time per operation due to path compression and union by rank.
  - Checking if the source and destination nodes are connected takes constant time.
- Space Complexity: O(n)
  - We use extra space to store the parent array and rank array.
