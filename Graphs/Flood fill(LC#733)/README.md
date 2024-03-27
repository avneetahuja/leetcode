# Flood Fill 🖌️

## Problem Statement

Given an `m x n` image `image` represented by an integer array `image` where `image[i][j]` represents the pixel value of the image, and coordinates `(sr, sc)` representing the starting pixel (i.e., the pixel value of `image[sr][sc]`), and a new pixel value `newColor`, you are asked to flood fill the image.

To perform a "flood fill," consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with the newColor.

Return the modified image after performing the flood fill.

## Approach 🚀

This problem can be solved using Depth-First Search (DFS). We perform a DFS starting from the given starting pixel `(sr, sc)` and change the color of connected pixels that have the same color as the starting pixel.

### Steps:
1. Check if the starting pixel `(sr, sc)` already has the `newColor`. If it does, return the original image.
2. Define a recursive function `search(i, j, startColor)` that performs DFS traversal starting from cell `(i, j)` with the `startColor`.
   - Change the color of the current cell `(i, j)` to the `newColor`.
   - Explore adjacent cells (up, down, left, right) if they are within the image boundaries and have the same `startColor`.
3. Call the `search` function with the starting pixel coordinates `(sr, sc)` and the color of the starting pixel (`image[sr][sc]`).
4. Return the modified image.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n)
  - The DFS traversal takes O(m * n) time, where `m` is the number of rows and `n` is the number of columns in the image.
- Space Complexity: O(m * n)
  - The space complexity is dominated by the recursive stack used in DFS traversal.
