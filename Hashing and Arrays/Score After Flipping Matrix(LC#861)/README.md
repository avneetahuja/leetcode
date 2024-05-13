# Matrix Score

## Problem Statement

You are given an `m x n` binary matrix `grid`. A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all `0`s to `1`s, and all `1`s to `0`s).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers. Return the highest possible score after making any number of moves (including none).

## Approach 🌟

To maximize the score of the matrix, we can apply the following strategy:

1. Ensure the leftmost column has the maximum score possible:
   - If the first element of a row is `0`, flip all elements in that row.
2. Ensure each subsequent column has more `1`s than `0`s:
   - For each column (except the leftmost one), count the number of `0`s and `1`s.
   - If there are more `0`s than `1`s, flip all elements in that column.

3. Calculate the final score:
   - Convert each row into a binary number and sum them up.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
  - We perform three passes over the matrix, each with linear time complexity.
- Space Complexity: O(1).
  - We use only a constant amount of extra space for storing variables.
