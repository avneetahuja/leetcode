# Largest Local in Grid

## Problem Statement

Given a grid of integers `grid`, return another grid of the same size where the value at position `(i, j)` is the maximum value of a 3x3 subgrid starting from the position `(i, j)` in the original grid.

## Approach 🌟

To solve this problem, we can iterate over each cell `(i, j)` in the grid and compute the maximum value of the 3x3 subgrid starting from this cell. We'll store these maximum values in a new grid.

1. Initialize a new grid `answer` of size `(n-2) x (n-2)` where `n` is the size of the original grid.
2. Iterate over each cell `(i, j)` in the original grid where `i` ranges from `0` to `n-3` and `j` ranges from `0` to `n-3`.
3. For each cell `(i, j)`, compute the maximum value `local_max` of the 3x3 subgrid starting from this cell.
4. Store `local_max` in the corresponding cell `(i, j)` of the new grid `answer`.
5. Return the `answer` grid.

## Complexity Analysis ⚙️

- Time Complexity: O(N^2), where N is the size of the original grid.
  - We iterate over each cell in the original grid and compute the maximum value of the 3x3 subgrid starting from that cell.
- Space Complexity: O(N^2), where N is the size of the original grid.
  - We store the maximum values of the subgrids in a new grid of the same size as the original grid.
