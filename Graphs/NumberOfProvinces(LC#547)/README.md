# Find Circle Num 🔄

## Problem Statement

You are given a map of cities `isConnected` where `isConnected[i][j] = 1` if there is a direct path between city `i` and city `j`, otherwise `0`. 

A city is represented as an integer which ranges from `0` to `n - 1`. 

Return the total number of provinces. 

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

## Approach 🚀

This problem can be solved using Depth-First Search (DFS). We can traverse through the cities using DFS and count the number of connected components or provinces.

### Steps:
1. Create an empty dictionary `visited` to keep track of visited cities.
2. Create an empty dictionary `adjList` to store the adjacency list representation of the graph.
3. Define a recursive function `search(i, flag)` that performs DFS traversal starting from city `i`.
   - Mark city `i` as visited.
   - Traverse through all adjacent cities of `i` and recursively call `search` on unvisited cities.
   - If `flag` is `True`, update the `adjList` to represent the adjacency list of the graph.
4. Iterate through each city and call `search` with `True` flag to create the adjacency list.
5. Return the length of `adjList`, which represents the total number of provinces.

## Complexity Analysis ⚙️

- Time Complexity: O(n^2)
  - The DFS traversal takes O(n^2) time, where n is the number of cities.
- Space Complexity: O(n^2)
  - We use additional space for the `visited` dictionary and `adjList`.
