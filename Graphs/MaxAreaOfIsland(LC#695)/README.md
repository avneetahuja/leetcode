# Max Area of Island 🏝️

## Problem Statement

Given a non-empty 2D array `grid` of 0's and 1's, an island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Calculate the maximum area of an island in the given 2D array. If there is no island, return `0`.

## Approach 🚀

This problem can be solved using Depth-First Search (DFS). We perform DFS starting from each land cell (`grid[i][j] = 1`) and calculate the area of the island connected to that cell.

### Steps:
1. Define a recursive function `search(i, j)` that performs DFS traversal starting from cell `(i, j)`.
   - Mark the current cell `(i, j)` as visited by setting `grid[i][j] = -1` (to avoid revisiting).
   - Explore adjacent cells (up, down, left, right) if they are within the grid boundaries and are land cells (`grid[i][j] = 1`).
   - Recursively call `search` for each adjacent land cell and accumulate the area.
2. Iterate through each cell in the grid:
   - If the cell is a land cell (`grid[i][j] = 1`), start DFS from that cell and update the maximum area.
3. Return the maximum area found.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n)
  - The DFS traversal takes O(m * n) time, where `m` is the number of rows and `n` is the number of columns in the grid.
- Space Complexity: O(1)
  - We are using only constant space for variables and recursion stack.
