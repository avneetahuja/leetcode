# Unique Paths 🌐

## Problem Statement

A robot is located at the top-left corner of an m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

## Approach 🛤️

We can solve this problem using dynamic programming. Let's define a 2D array `t` where `t[i][j]` represents the number of unique paths to reach the bottom-right corner from cell `(i, j)`.

### Recurrence Relation:

- If `i == m-1`, return `1`.
  - If the robot is in the last row, there is only one way to reach the bottom-right corner, i.e., by moving right.
- If `j == n-1`, return `1`.
  - If the robot is in the last column, there is only one way to reach the bottom-right corner, i.e., by moving down.
- If `t[i][j]` is already calculated, return `t[i][j]`.
- Otherwise, `t[i][j] = f(i+1, j) + f(i, j+1)` since the robot can move either down or right.

### Base Cases:

- If `i == m-1`, return `1`.
  - If the robot is in the last row, there is only one way to reach the bottom-right corner, i.e., by moving right.
- If `j == n-1`, return `1`.
  - If the robot is in the last column, there is only one way to reach the bottom-right corner, i.e., by moving down.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n)
  - We fill up the 2D array `t` of size m * n.
- Space Complexity: O(m * n)
  - We use a 2D array `t` for dynamic programming.
