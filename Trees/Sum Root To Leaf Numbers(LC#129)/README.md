# Sum Root to Leaf Numbers

## Problem Statement

Given a binary tree where each node contains a digit from 0-9, return the sum of all root-to-leaf numbers.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

## Approach 🌟

To find the sum of all root-to-leaf numbers, we can use a depth-first search (DFS) approach. We'll perform a recursive DFS traversal of the tree, keeping track of the current sum of digits from the root to the current node. When we reach a leaf node, we'll add the sum to the total sum.

Here's how the approach works:
1. Initialize a variable `total` to store the sum of all root-to-leaf numbers.
2. Define a recursive function `dfs` that takes a node and the current sum as parameters:
   - If the node is a leaf node (i.e., it has no children), add the current sum plus the value of the leaf node to the `total`.
   - If the node has a left child, recursively call `dfs` with the left child and the updated sum.
   - If the node has a right child, recursively call `dfs` with the right child and the updated sum.
3. Call the `dfs` function with the root node and an empty string as the initial sum.
4. Return the `total` sum.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
- Space Complexity: O(h), where h is the height of the binary tree. The space complexity is determined by the recursive stack used for the depth-first search.
