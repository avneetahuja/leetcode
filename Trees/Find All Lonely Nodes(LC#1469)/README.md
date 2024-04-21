# Get Lonely Nodes in Binary Tree

## Problem Statement

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. A lonely node is a node that is the only child of its parent node. The tree is non-empty and contains at most 10^4 nodes.

## Approach 🌟

To solve this problem, we can use a recursive depth-first search (DFS) approach:

1. Initialize an empty list `res` to store the values of lonely nodes.
2. Implement a recursive function `search(node)` to traverse the binary tree.
3. In the `search` function, check if the current node has exactly one child (either left or right child, but not both).
   - If the node has only a left child, add the value of the left child to `res`.
   - If the node has only a right child, add the value of the right child to `res`.
4. Recursively call the `search` function on the left and right children of the current node.
5. Return the `res` list containing the values of all lonely nodes.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the number of nodes in the binary tree.
  - We visit each node of the binary tree once during the DFS traversal.
- Space Complexity: O(H), where H is the height of the binary tree (stack space for recursive calls).
  - In the worst case, the recursive call stack can reach the height of the tree.
