# Surrounded Regions 🔄⬜

## Problem Statement

Given an `m x n` matrix `board` containing only the characters `'O'` and `'X'`, capture all regions that are 4-directionally surrounded by `'X'`. A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

Surrounded regions should not be on the border, which means that any `'O'` on the border of the matrix are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## Approach 🛠️

We can perform a Depth-First Search (DFS) to identify and mark all the regions connected to the border. We can iterate over the border cells and if we find any `'O'`, we perform DFS to mark all the connected `'O'` cells with a temporary marker, such as `'#'`. Then, we iterate over the entire matrix and flip the remaining `'O'` cells to `'X'` and revert the temporary marker `'#'` back to `'O'`. This way, we identify and capture all the surrounded regions.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
  - We perform a DFS for each border cell, and the DFS operation has a time complexity of O(m * n).
- Space Complexity: O(1)
  - We perform the DFS in-place, and no additional space is used.
