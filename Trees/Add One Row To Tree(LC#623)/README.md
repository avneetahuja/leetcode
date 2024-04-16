# Add One Row to Tree

## Problem Statement

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

## Approach 🌟

To add a row of nodes with value `val` at depth `depth` in the binary tree, we can use a breadth-first search (BFS) traversal approach.

Here's how the approach works:
1. If `depth` is 1, we create a new root with value `val` and set its left child to the current root. Then, we return the new root.
2. Otherwise, we perform a BFS traversal of the tree until we reach a level just before the target depth.
3. At this level, for each node encountered, we insert new nodes with value `val` as the left and right children.
4. We continue the BFS traversal until all nodes at the target depth have been processed.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of nodes in the binary tree.
  - Performing a BFS traversal takes O(n) time.
- Space Complexity: O(n), where n is the number of nodes in the binary tree.
  - In the worst case, the queue can contain all nodes in the last level of the tree.

## Summary

In this problem, we learned how to add a row of nodes with a given value at a specified depth in a binary tree. By using a BFS traversal approach, we were able to achieve this efficiently.
