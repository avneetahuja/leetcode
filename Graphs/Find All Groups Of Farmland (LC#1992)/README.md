# Find Farmland

## Problem Statement

You are given a rectangular piece of land with `0`s and `1`s. The `1`s represent fields and the `0`s represent water. Some fields are adjacent to each other, forming rectangular pieces of land called farmland. Two adjacent fields are considered part of the same farmland if one is immediately adjacent to the other horizontally or vertically, but not diagonally.

Given the representation of the land as a 2D array `land`, where `land[i][j]` is `0` if the cell is water and `1` if it is land, return a list of rectangular pieces of land in the format `[x1, y1, x2, y2]`, where:

- `(x1, y1)` is the coordinate of the top-left corner of the land.
- `(x2, y2)` is the coordinate of the bottom-right corner of the land.

If there are no pieces of farmland, return an empty list.

## Approach 🌟

To solve this problem, we can use a depth-first search (DFS) approach:

1. Iterate through each cell of the land.
2. If a cell represents farmland (i.e., `land[i][j] == 1`), start a DFS search from that cell to find the boundaries of the farmland.
3. In the DFS search, recursively explore all adjacent cells that are part of the same farmland.
4. Update the value of the explored cells to `-1` to mark them as visited.
5. Keep track of the top-left and bottom-right corners of the farmland during the DFS search.
6. Once the DFS search for a farmland is complete, add its boundaries to the result list.
7. Return the result list containing the boundaries of all farmlands found.

## Complexity Analysis ⚙️

- Time Complexity: O(R * C), where R is the number of rows and C is the number of columns in the land grid.
  - We visit each cell of the grid once during the DFS search.
- Space Complexity: O(1) (excluding the output).
  - We use only a constant amount of extra space for variables.
