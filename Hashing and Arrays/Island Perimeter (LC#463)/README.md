# Island Perimeter

## Problem Statement

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

## Approach 🌟

To find the perimeter of the island, we need to count the number of "sides" of the island cells that are exposed to water.

1. Initialize a variable `res` to store the perimeter count.
2. Iterate through each cell in the grid:
   - If the cell is land (i.e., `grid[i][j] == 1`), check its neighboring cells.
   - Increment `res` for each side of the cell that is exposed to water.
     - A side is exposed to water if the neighboring cell is out of bounds or if it is water (`grid[x][y] == 0`).
3. Return `res` as the total perimeter count.

## Complexity Analysis ⚙️

- Time Complexity: O(R * C), where R is the number of rows and C is the number of columns in the grid.
  - We iterate through each cell in the grid once.
- Space Complexity: O(1).
  - We use only a constant amount of extra space.
