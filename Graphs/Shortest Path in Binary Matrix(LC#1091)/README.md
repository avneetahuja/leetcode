# Shortest Path in Binary Matrix 🛤️

## Problem Statement

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

## Approach 🌟

To find the shortest clear path in the binary matrix, we can use Breadth-First Search (BFS) algorithm.

1. Start from the top-left cell `(0, 0)` and perform BFS.
2. Use a queue to keep track of cells to visit next.
3. Initialize a `seen` set to keep track of visited cells.
4. Iterate through the queue while it's not empty:
    - Pop a cell `(x, y)` from the queue.
    - If `(x, y)` is the bottom-right cell `(n - 1, n - 1)`, return the distance.
    - Otherwise, explore the 8-directional neighbors of `(x, y)`:
        - If the neighbor is within bounds, not visited, and clear (grid value is 0), add it to the queue and mark it as visited.
        - Update the distance of the neighbor cell in the grid to be `distance + 1`.
5. If the bottom-right cell is not reached during BFS, return -1.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of cells in the binary matrix.
  - Each cell is visited at most once during BFS.
- Space Complexity: O(N), where N is the number of cells in the binary matrix.
  - The space complexity is dominated by the queue and the `seen` set used in BFS.
