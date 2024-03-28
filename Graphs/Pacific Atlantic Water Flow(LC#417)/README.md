# Pacific Atlantic Water Flow 🌊

## Problem Statement

Given an `m x n` matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix, and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

## Approach 🚀

To solve this problem, we can perform a depth-first search (DFS) from each ocean (Pacific and Atlantic) to mark all cells reachable from that ocean. Then, we can find the intersection of cells reachable from both oceans.

### Steps:
1. Define two sets: one for the cells reachable from the Pacific ocean (`pac`) and another for the cells reachable from the Atlantic ocean (`atl`).
2. Perform DFS from the top and left edges to mark cells reachable from the Pacific ocean and from the bottom and right edges to mark cells reachable from the Atlantic ocean.
3. Find the intersection of cells reachable from both oceans.
4. Return the list of grid coordinates representing the cells in the intersection.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n)
  - We perform a depth-first search from each ocean, visiting each cell at most once.
- Space Complexity: O(m * n)
  - We use sets to store cells reachable from each ocean.
