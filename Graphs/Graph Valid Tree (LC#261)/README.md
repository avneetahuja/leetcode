# Valid Tree ✅

## Problem Statement

You are given an integer `n` representing the number of nodes in the graph and a list of `n-1` edges where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

You want to check if the given graph is a valid tree.

A valid tree is a graph that has the following properties:
1. It has `n-1` edges.
2. It has exactly one connected component.

## Approach 🌲

To solve this problem, we can use the Union-Find algorithm. We'll follow these steps:
1. Initialize an array `root` of size `n`, where `root[i]` represents the parent of node `i` initially set to `i`.
2. Initialize an array `rank` of size `n`, where `rank[i]` represents the rank (depth) of the subtree rooted at node `i`, initially set to `1`.
3. Initialize a variable `c` to `n`, which represents the number of connected components.
4. Define a function `find(i)` to find the root of the component containing node `i`. If `root[i]` is not equal to `i`, recursively find the root of the component containing the parent of node `i`.
5. Define a function `union(i, j)` to union the components containing nodes `i` and `j`. If the roots of `i` and `j` are not the same, merge the smaller rank tree into the larger rank tree. If the ranks are equal, choose any tree and increment its rank. Decrement `c` after the union operation.
6. Iterate through each edge in `edges` and union the components containing the nodes connected by the edge.
7. Return `True` if `c` is equal to `1`, indicating that there is exactly one connected component; otherwise, return `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(nα(n)), where α(n) is the inverse Ackermann function.
  - The Union-Find operations take nearly constant time per operation due to path compression and union by rank.
- Space Complexity: O(n)
  - We use extra space to store the parent array and rank array.
