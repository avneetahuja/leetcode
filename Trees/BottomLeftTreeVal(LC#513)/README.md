# Find Bottom Left Value in Binary Tree 🌳↙️

## Problem Statement

Given a binary tree, find the leftmost value in the last row of the tree.

## Approach 🛠️

The solution performs a depth-first search (DFS) on the binary tree, keeping track of the leftmost value at the last level encountered.

1. Start the DFS traversal from the root of the binary tree.
2. For each node visited, update the leftmost value and the last level if the current level is greater than the last level.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - The solution traverses each node once during the depth-first search.
- Space Complexity: O(1).
  - The solution uses a constant amount of space for the leftmost value and level variables.
