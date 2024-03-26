# Number of Islands 🏝️

## Problem Statement

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Approach 🚀

This problem can be solved using Depth-First Search (DFS). We can traverse through the grid and perform DFS whenever we encounter a land ('1'). By marking visited cells and exploring adjacent cells, we can identify connected components, which represent islands.

### Steps:
1. Create an empty dictionary `visited` to keep track of visited cells.
2. Initialize a variable `count` to 0, which will represent the number of islands.
3. Define a recursive function `search(i, j)` that performs DFS traversal starting from cell `(i, j)`.
   - Mark cell `(i, j)` as visited.
   - Explore adjacent cells (up, down, left, right) if they are within the grid boundaries and are land ('1').
4. Iterate through each cell of the grid.
   - If the cell is land ('1') and not visited, increment `count` and perform DFS from that cell.
5. Return the value of `count`, which represents the number of islands.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n)
  - The DFS traversal takes O(m * n) time, where `m` is the number of rows and `n` is the number of columns in the grid.
- Space Complexity: O(m * n)
  - We use additional space for the `visited` dictionary.
